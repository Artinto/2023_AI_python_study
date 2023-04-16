# https://github.com/pytorch/examples/blob/master/mnist/main.py
from __future__ import print_function # Print문을 파이썬 버전3(우리가 아는 방식)를 파이썬 버전 2에서 사용할 수 있도록한다.
import argparse # 특정 옵션에 따라 스크립트를 다르게 작동하기 위해서 사용. 본 코드에서는 사용되지 않음.
import torch # Pytorch 사용을 위해서 import
import torch.nn as nn # 신경망 모듈을 사용하기 위해 import 
import torch.nn.functional as F # 활성화 함수(여기엔 ReLU)를 이용하기 위해 import
import torch.optim as optim # Optimizer 사용을 위해 사용.
from torchvision import datasets, transforms  # MNIST, CIFAR10과 같이 pytorch에서 제공하는 데이터셋 모듈과 데이터 전처리를 위한 transforms import
from torch.autograd import Variable # Pytorch에서 역전파과정 중 gradient를 계산하기 위해서 사용. 이는 PrTorch 버전 0.4 이후 부터는 사용하지 않는다.

# Training settings
batch_size = 64 # 학습할 데이터 단위 설정

# MNIST Dataset
# 학습 데이터 셋 생성. torchvision에 존재하는 MNIST 데이터 셋을 다운
train_dataset = datasets.MNIST(root='./mnist_data/', # 데이터 셋을 저장할 경로 지정.
                               train=True,           # 데이터 셋을 학습용과 테스트용으로 분리하는 용도로 train =True 면 학습용을 가져온다.
                               transform=transforms.ToTensor(), # 데이터 셋을 저장할 때 Tensor로 변환(0~1사이의 실수형으로 정규화)해서 저장한다.
                               download=True) # 현재 지정된 root에 데이터셋이 없다면 다운로드, 있다면 다운로드하지 않음.
# 테스트 데이터 셋 생성. torchvision에 존재하는 MNIST 데이터 셋을 다운
test_dataset = datasets.MNIST(root='./mnist_data/', # 데이터셋을 저장할 경로
                              train=False, # 데이터 셋을 테스트용을 저장하겠다.
                              transform=transforms.ToTensor())

# Data Loader (Input Pipeline)
# 앞서 저장한 train_dataset과 test_dataset(텐서로 구성)을 앞서 선언한 batch_size로 불러온다.
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True) # train의 경우 과적합을 방지하기 위해서 shuffle을 해줌.

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False) # test의 경우 결과를 출력해야하므로 shufffle을 따로 해줄 필요가 없음.

# 모델 선언
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) # Conv2d는 입력 출력 데이터는 배치 크기, 이미지 채널 수, 이미지의 높이, 이미지의 넓이의 형태이다..Conv2d(4차원 데이터)를 통해 입력은 1, 출력은 10개, 필터는 5x5 크기로  설정.
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5) # Conv2d(4차원 데이터)를 통해 입력은 10, 출력은 20, 필터는 5x5 크기로 설정.
        # 참고로 Conv2d의 출력의 크기는 ((입력 이미지의 높이 + 2 * 패딩정도 - 필터 크기) / 필터이동 간격(Stride) + 1 )x ((입력 이미지의 너비 + 2 * 패딩정도 - 필터 크기) / 필터이동 간격(Stride) + 1)
        self.mp = nn.MaxPool2d(2) # 필터 크기를 2x2로 최대값만 추출하는 레이어를 정의.
        self.fc = nn.Linear(320, 10) # fully connect 방법으로 입력은 320, 출력은 10개(손글씨의 종류 수)로 함.
        # 320의 경우는 아래를 통해 확인한다.

    def forward(self, x):
        in_size = x.size(0) # 배치 사이즈를 정의한다. 나중 flatten과정을 위해.
        x = F.relu(self.mp(self.conv1(x))) # conv1 후 mp과정을 진행. 입력이 64, 1, 28, 28에서 conv1 후 64, 10, 24, 24 가되고 mp과정을 통해 64,10,12,12가 된다.
        x = F.relu(self.mp(self.conv2(x))) # conv2 후 mp과정을 진행. 입력이 64,10,12,12에서 conv2 후 64,20,8,8이고 mp과정을 통해 64,20,4,4가 된다.
        x = x.view(in_size, -1)  # flatten the tensor 이를 (64, x)로 flatten하게 되면, 뒤는 20x4x4이므로 320이 된다.
        x = self.fc(x) # 입력이 320, 출력은 10개로 되고 
        return F.log_softmax(x) 
# 계산을 편리성을 위해서 log을 사용하며, 결과는 각 label이 가능한 확률이 나온다.

model = Net() # 모델 선언
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5) # Stochastic Gradient Descent를 optimizer로 생성하고, 학습률은 0.01로 한다.
# momentum을 이용해 이전의 SGD 업데이트 방향성을 반영한다. 보통 0.5~ 0.9로 반영(클수록 더 많이 반영한다)

def train(epoch):
    model.train() # 선언한 모델 학습모드로 함.(모델의 layer들이 학습된다.) 
    for batch_idx, (data, target) in enumerate(train_loader): # X값과 라벨 값을 train_loader가 가지고 있으므로 이를 data와 target으로 선언받고, enumerate를 이용해서 batch의 인덱스도 받을수 있도록 한다.
        data, target = Variable(data), Variable(target) # 앞서 언급하였듯이 Variable은  PrTorch 버전 0.4 이후 부터는 사용하지 않아 주석으로 처리하여 실행해도 무방하다.
        optimizer.zero_grad() # Optimizer의 gradient를 0으로 설정(초기화), 이전 batch 의 gradient가 현재 batch에 영향받는 것을 방지함.
        output = model(data) # 모델에 X값을 넣어 Y를 예상.
        loss = F.nll_loss(output, target) # 실제값과 예상값을 비교. 이때 Negative Log Likelihood Loss를 손실함수로 한다 nll_loss의 경우 -log(y_t)로 계산되어 작을 수록 좋다!
        loss.backward() # backward을 진행 - 손실에 대한 gradient 계산
        optimizer.step() # 계산된 gradient로 weight update
        if batch_idx % 10 == 0: # 학습 과정 모니터링을 위해서 사용, batch가 10번 들어올때마다 사용.
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format( # 학습수, 어느정도 진행됬는지, 현재 학습에서 손실 정도를 출력한다.
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))


def test():
    model.eval() # 학습한 모델을 평가모드로함.(모델의 layer들이 학습되지 않는다.)
    test_loss = 0 # 초기의 loss 지정
    correct = 0 # 초기의 correct 지정.
    for data, target in test_loader: # X값과 라벨 값을 test_loader가 가지고 있으므로 이를 data와 target으로 선언받고, test에서는 배치의 index를 알 필요가 없으므로 사용하지 않음.
        data, target = Variable(data, volatile=True), Variable(target) # Variable은  PrTorch 버전 0.4 이후 부터는 사용하지 않아 주석으로 처리하여 실행해도 무방하다. 여기서 volatile=True를 통해 gradient가 계산이 일어나지 않도록 하여 속도를 좀 더 높여준다. 
        # volatile=True를 현재는 with torch.no_grad()를 이용해 사용한다.
        output = model(data) # 학습된 모델에 X값을 넣어 Y를 예상.
        # sum up batch loss
        test_loss += F.nll_loss(output, target, size_average=False).data # size_averge=False를 이용해서 예상값과 출력값의 nll_loss값들의 합을 계산하고 이를 test_loss에 누적한다.

        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1] # 해당 경우 결과 shape이 (64(batch_size), 1)인 텐서이고 indexing[1]을 통해 해당 큰 값을 가지고 있는 index만 pred로 저장한다.
        # 예상값(Tensor)에서 데이터를 가져와 이중 가장 큰 확률을 가지고 있는 값의 인덱스 값을 보여줌. 결국 예상하는 mnist값이 저장된다. 
        correct += pred.eq(target.data.view_as(pred)).cpu().sum() #위에서 pred에 저장되어 있는 값은 결국 0~9사이의 예상되는 mnist 값중 하나이므로 이를 실제 데이터인 target과 비교하여 맞으면 1 아니면 0의 Tensor로 반환함.
        # 이전에 있는 실제값(Tensor)에서 데이터를 가져와 view_as를 통해 pred와 같은 shape으로 변환하고 element-wise equal(eq)를 통해 1과 0을 출력하고 이를 cpu().sum()을 통해서 반환된 Tensor의 값들을 CPU상에 모두 더한다. 
        # 이를 통해 Correct에는 전체 배치에서 예상값 = 실제값인 샘플의 수를 저장한다.

    test_loss /= len(test_loader.dataset) # 전체 배치로 나눠서 평균 손실값으로 바꿈.
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format( # 평균 손실과 정확도를 출력한다.
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 10): # 총 epoch가 9번 동안
    train(epoch) # 선언한 함수에 몇 번째 epoch인지 전달, 학습과 학습 모니터링을 진행함.
    test() # 선언한 함수를 통해 평균 손실와 정확도에 대해 출력