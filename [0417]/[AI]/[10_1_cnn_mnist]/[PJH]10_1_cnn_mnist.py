# https://github.com/pytorch/examples/blob/master/mnist/main.py
from __future__ import print_function
import argparse # argparse 모듈 : 명령행 인자를 파싱하는 라이브러리
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

# Training settings
batch_size = 64 # 하이퍼 파라미터로 배치 사이즈 지정


# MNIST Dataset
train_dataset = datasets.MNIST(root='./data/',
                               train=True, # 학습용 데이터셋
                               transform=transforms.ToTensor(), # 이미지 데이터셋을 Tensor로 변환
                               download=True) # 데이터셋이 로컬에 없는 경우 인터넷에서 다운로드

test_dataset = datasets.MNIST(root='./data/',
                              train=False, # 테스트용 데이터셋
                              transform=transforms.ToTensor())

# Data Loader (Input Pipeline)
# DataLoader는 데이터셋을 통해 반복적으로 데이터 불러오고 샘플링을 수행하는 역할
# 입력값으로 받은 데이터셋을 미니배치 단위로 분할하고
# 데이터 랜덤 셔플, 병렬 처리 등을 지원하여 학습 속도를 높임
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)


def __init__(self):
    super(Net, self).__init__()
    # 첫번째 convolutional layer
    self.conv1 = nn.Conv2d(1, 10, kernel_size=5)   # 입력채널 : 1, 출력채널 : 10, 필터크기 : 5
    # 두번째 convolutional layer
    self.conv2 = nn.Conv2d(10, 20, kernel_size=5)  # 입력채널 : 10, 출력채널 : 20, 필터크기 : 5
    # max pooling
    self.mp = nn.MaxPool2d(2)    # 풀링커널 크기 : 2
    # fully-connected layer
    self.fc = nn.Linear(320, 10) # 입력크기 : 320, 출력크기 : 10

def forward(self, x):
    in_size = x.size(0)
    # convolutional layer -> ReLU -> max pooling
    x = F.relu(self.mp(self.conv1(x)))    # conv1 -> ReLU -> maxpooling
    # convolutional layer -> ReLU -> max pooling
    x = F.relu(self.mp(self.conv2(x)))    # conv2 -> ReLU -> maxpooling
    x = x.view(in_size, -1)  # flatten the tensor
    x = self.fc(x)            # fully-connected layer
    return F.log_softmax(x)


model = Net()

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

# 모델 평가
def test():
    model.eval() # 테스트 손실값과 정확도 초기화
    test_loss = 0
    correct = 0 # 테스트 데이터셋에서 배치 단위로 데이터와 레이블을 불러옴
    for data, target in test_loader: # 입력 데이터와 레이블을 Variable로 만들어줌 , volatile=True 옵션은 연산 그래프를 구성하지 않도록 설정하여 메모리 사용량을 줄임
        data, target = Variable(data, volatile=True), Variable(target) # 모델을 사용하여 데이터에 대한 예측값 계산
        output = model(data) # 배치 손실값을 누적
        # sum up batch loss
        test_loss += F.nll_loss(output, target, size_average=False).data # 최대 로그 확률 값을 가지는 인덱스를 구함
        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1] # 정답 레이블과 예측값이 일치하는 개수를 계산하여 누적
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    # 전체 테스트 데이터셋에 대한 평균 손실값 계산
    test_loss /= len(test_loader.dataset)
    # 테스트 결과 출력
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 10):
    train(epoch)
    test()
