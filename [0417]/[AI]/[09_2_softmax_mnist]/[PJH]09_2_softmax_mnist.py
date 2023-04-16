# https://github.com/pytorch/examples/blob/master/mnist/main.py
from __future__ import print_function # Python 2.x 버전에서 사용되는 print 함수의 기능과 3.x 버전에서 사용되는 print() 함수의 기능을 호환성을 유지하기 위한 코드
from torch import nn, optim, cuda # pytorch의 모듈들을 import합니다.
from torch.utils import data
from torchvision import datasets, transforms
import torch.nn.functional as F 
import time # 시간 측정을 위한 모듈입니다.


# Training settings
batch_size = 64
device = 'cuda' if cuda.is_available() else 'cpu' # GPU 사용 가능 여부를 확인하고 device에 할당합니다.
print(f'Training MNIST Model on {device}\n{"=" * 44}')

# MNIST Dataset
train_dataset = datasets.MNIST(root='./mnist_data/', # 데이터를 저장할 폴더 경로입니다.
                               train=True, # 학습용 데이터셋을 불러옵니다.
                               transform=transforms.ToTensor(),# 이미지 데이터를 PyTorch Tensor로 변환합니다. 
                               download=True) # MNIST 데이터셋을 다운로드합니다.

test_dataset = datasets.MNIST(root='./mnist_data/', # 데이터를 저장할 폴더 경로입니다.
                              train=False, # 테스트용 데이터셋을 불러옵니다.
                              transform=transforms.ToTensor()) # 이미지 데이터를 PyTorch Tensor로 변환합니다.

# Data Loader (Input Pipeline)
train_loader = data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size, # 배치 크기를 지정합니다. 
                                           shuffle=True)  # 데이터셋을 섞어서 불러올지 여부를 지정합니다.

test_loader = data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,# 배치 크기를 지정합니다.
                                          shuffle=False)# 데이터셋을 섞지 않고 불러올지 여부를 지정합니다.

# 신경망 모델 클래스를 정의합니다.
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.l1 = nn.Linear(784, 520)
        self.l2 = nn.Linear(520, 320)
        self.l3 = nn.Linear(320, 240)
        self.l4 = nn.Linear(240, 120)
        self.l5 = nn.Linear(120, 10)

    def forward(self, x):
        x = x.view(-1, 784)  # Flatten the data (n, 1, 28, 28)-> (n, 784)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)


model = Net()
model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


# 학습 함수 정의
def train(epoch):
    model.train() # 모델을 학습 모드로 설정
    for batch_idx, (data, target) in enumerate(train_loader): # 배치 단위로 데이터와 레이블을 가져옴
        data, target = data.to(device), target.to(device) # 데이터와 레이블을 GPU로 전송
        optimizer.zero_grad() # 기울기 초기화
        output = model(data) # 모델에 데이터 입력
        loss = criterion(output, target) # 손실 계산
        loss.backward() # 역전파 실행
        optimizer.step() # 가중치 갱신
        if batch_idx % 10 == 0:
            # 배치 단위로 손실 출력
            print('Train Epoch: {} | Batch Status: {}/{} ({:.0f}%) | Loss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))


# 테스트 함수 정의
def test():
    model.eval() # 모델을 평가 모드로 설정
    test_loss = 0 # 전체 테스트 데이터 손실 초기화
    correct = 0 # 전체 테스트 데이터 정확도 초기화
    for data, target in test_loader: # 배치 단위로 데이터와 레이블을 가져옴
        data, target = data.to(device), target.to(device) # 데이터와 레이블을 GPU로 전송
        output = model(data) # 모델에 데이터 입력
        # 배치 단위로 손실 누적
        test_loss += criterion(output, target).item()
        # 배치 단위로 정확도 누적
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(test_loader.dataset) # 전체 테스트 데이터 손실 평균
    # 전체 테스트 데이터 손실과 정확도 출력
    print(f'===========================\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)} '
          f'({100. * correct / len(test_loader.dataset):.0f}%)')


if __name__ == '__main__':
    since = time.time() # 시작 시간 측정
    for epoch in range(1, 10):
        epoch_start = time.time() # 에포크 시작 시간 측정
        train(epoch) # 학습 실행
        m, s = divmod(time.time() - epoch_start, 60)
        # 에포크 학습 시간 출력
        print(f'Training time: {m:.0f}m {s:.0f}s')
        test() # 테스트 실행
        m, s = divmod(time.time() - epoch_start, 60)
        # 에포크 테스트 시간 출력
        print(f'Testing time: {m:.0f}m {s:.0f}s')

    m, s = divmod(time.time() - since, 60)#
    print(f'Total Time: {m:.0f}m {s:.0f}s\nModel was trained on {device}!')
