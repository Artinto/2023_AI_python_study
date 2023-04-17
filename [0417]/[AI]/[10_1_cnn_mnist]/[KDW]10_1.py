# https://github.com/pytorch/examples/blob/master/mnist/main.py
from __future__ import print_function
import argparse
import torch 
import torch.nn as nn 
import torch.nn.functional as F 
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable 

# Training settings
batch_size = 64 # 배치 단위 설정

# MNIST Dataset
# torchvision에서 제공하는 MNIST 데이터 다운
train_dataset = datasets.MNIST(root='./mnist_data/', # 저장 경로
                               train=True,           # 학습용
                               transform=transforms.ToTensor(), # 데이터 텐서로 저장
                               download=True) # 경로에 데이터 없으면 다운
test_dataset = datasets.MNIST(root='./mnist_data/', # 경로
                              train=False, # 테스트용으로 가져옴
                              transform=transforms.ToTensor())

#데이터 로더 생성 (배치사이즈 지정 및 위에서 지정한 데이터 셋 가져옴)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)

# 신경망 클래스 
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) # Conv2d함수로 배치 크기, 이미지 채널 수, 이미지의 높이, 이미지의 넓이 설정
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5) #10, 출력은 20, 필터는 5x5 크기 설정
        self.mp = nn.MaxPool2d(2) # 사용하는 필터 크기를 2x2설정
        self.fc = nn.Linear(320, 10) #  입력은 320, 출력은 10로 지정
        # 320의 경우는 아래를 통해 확인한다.

    def forward(self, x):
        in_size = x.size(0) # 배치 사이즈를 정의 (아래에서 사용)
        x = F.relu(self.mp(self.conv1(x)))
        x = F.relu(self.mp(self.conv2(x))) 
        return F.log_softmax(x) 
# 계산을 편리성을 위해서 log을 사용하며, 결과는 각 label이 가능한 확률이 나온다.

model = Net() # 모델 선언
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5) # Stochastic Gradient Descent를 optimizer로 생성하고, 학습률은 0.01로 한다.
# momentum을 이용해 이전의 SGD 업데이트 방향성을 반영한다. 보통 0.5~ 0.9로 반영(클수록 더 많이 반영한다)

def train(epoch):
    model.train() # 모델은 학습모드로 실행
    for batch_idx, (data, target) in enumerate(train_loader): # 위에서 지정한 로드 형식으로 데이터 가져옴
        data, target = Variable(data), Variable(target) 
        optimizer.zero_grad() # gradient 초기화
        output = model(data) # 모델에 데이터 적용후 반환 값 저장
        loss = F.nll_loss(output, target) # Negative Log Likelihood Loss를 손실함수로 사용하여 계산
        loss.backward() # 역전파
        optimizer.step() #  gradient 계산 후 업데이트
        if batch_idx % 10 == 0: # 배치 10번 마다 출력
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format( # 학습 횟수, 진행도, 손실 값 출력
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))


def test():
    model.eval() # 평가모드로 모델 지정
    test_loss = 0 # loss 초기화
    correct = 0 # correct 초기화
    for data, target in test_loader: # 위에서 지정한 로드 형식으로 데이터 가져옴
        data, target = Variable(data, volatile=True), Variable(target) 

        output = model(data) # 모델에 데이터 적용후 반환 값 저장

        test_loss += F.nll_loss(output, target, size_average=False).data # Negative Log Likelihood Loss를 손실함수로 사용하여 계산

        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1] # 모델에서 적용 후 반환값의 데이터를 예측값으로 저장
        correct += pred.eq(target.data.view_as(pred)).cpu().sum() # 정확도 값 누적

    test_loss /= len(test_loader.dataset) # 총값에서 평균을 냄
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format( # 평균 손실과 정확도를 출력
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 10):
    train(epoch) # 학습함수 실행
    test() #테스트함수 실행
