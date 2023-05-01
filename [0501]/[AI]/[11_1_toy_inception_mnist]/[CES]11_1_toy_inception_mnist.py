# Python 2.x에서도 Python 3.x의 print 함수를 사용할 수 있도록 하는 코드
from __future__ import print_function
# 명령행 인수 파싱에 유용한 모듈
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
# 이미지 데이터셋 및 전처리를 다루는 모듈
from torchvision import datasets, transforms
from torch.autograd import Variable

# 학습 설정을 위한 변수인 batch_size를 64로 설정
batch_size = 64
# 이미지 분류를 위해 MNIST 데이터셋을 다운로드하고, 학습용(train)과 검증용(test) 데이터셋을 만듦
# 이미지를 텐서 형태로 변환
train_dataset = datasets.MNIST(root='./data/',
                               train=True,
                               transform=transforms.ToTensor(),
                               download=True)

test_dataset = datasets.MNIST(root='./data/',
                              train=False,
                              transform=transforms.ToTensor())
# 데이터를 로드하는 DataLoader를 만듦
# 데이터셋을 지정하고, 배치 크기를 설정
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)
# train_loader이기 때문에 과적합을 방지하기 위해 shuffle을 True로 지정
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)

# InceptionA 클래스 정의
class InceptionA(nn.Module):
# 클래스의 생성자 정의 -> super()를 사용하여 부모 클래스 nn.Module의 생성자 호출
    def __init__(self, in_channels):
        super(InceptionA, self).__init__()
# 입력 : in_channels, 출력 16
        self.branch1x1 = nn.Conv2d(in_channels, 16, kernel_size=1)
# 입력 : in_channels, 출력 16
        self.branch5x5_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
# 입력 : 16, 출력 24
        self.branch5x5_2 = nn.Conv2d(16, 24, kernel_size=5, padding=2)
# 입력 : in_channels, 출력 16
        self.branch3x3dbl_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
# 입력 : 16, 출력 24
        self.branch3x3dbl_2 = nn.Conv2d(16, 24, kernel_size=3, padding=1)
# 입력 : 24, 출력 24
        self.branch3x3dbl_3 = nn.Conv2d(24, 24, kernel_size=3, padding=1)
# 입력 : in_channels, 출력 24
        self.branch_pool = nn.Conv2d(in_channels, 24, kernel_size=1)

    def forward(self, x):
        branch1x1 = self.branch1x1(x)
# branch1x1: 1x1 컨볼루션을 수행. 이 때, 커널의 개수는 16으로 설정
        branch5x5 = self.branch5x5_1(x)
        branch5x5 = self.branch5x5_2(branch5x5)
# 1x1 컨볼루션을 수행하고, 그 다음 5x5 커널을 사용하여 컨볼루션을 수행. 이 때, 첫번째 컨볼루션의 커널 개수는 16, 두번째 컨볼루션의 커널 개수는 24로 설정
        branch3x3dbl = self.branch3x3dbl_1(x)
        branch3x3dbl = self.branch3x3dbl_2(branch3x3dbl)
        branch3x3dbl = self.branch3x3dbl_3(branch3x3dbl)
# 1x1 컨볼루션을 수행하고, 그 다음 3x3 커널을 사용하여 컨볼루션을 두 번 수행. 이 때, 첫번째 컨볼루션의 커널 개수는 16, 두번째 컨볼루션의 커널 개수는 24로 설정
        branch_pool = F.avg_pool2d(x, kernel_size=3, stride=1, padding=1)
        branch_pool = self.branch_pool(branch_pool)
# 입력 x에 대해 3x3 평균 풀링을 수행하고, 그 결과에 1x1 컨볼루션을 수행. 이 때, 커널의 개수는 24로 설정
        outputs = [branch1x1, branch5x5, branch3x3dbl, branch_pool]
        return torch.cat(outputs, 1)
# 위의 연산 결과를 모두 concatenation 한 후 반환
# 1차원 기준으로 연산을 수행하므로 출력 텐서의 채널 개수는 16+24+24+24 = 88

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 입력채널 : 1 ,출력 채널 : 10 , 커널 크기 : 5x5
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        # 입력채널 : 88(10+24+24+30) ,출력 채널 : 10 , 커널 크기 : 5x5
        self.conv2 = nn.Conv2d(88, 20, kernel_size=5)
        # 입력채널 : 10
        self.incept1 = InceptionA(in_channels=10)
        # 입력 채널 : 20
        self.incept2 = InceptionA(in_channels=20)
        # 2x2 max pooling(nn.MaxPool2d) 객체 mp 선언
        self.mp = nn.MaxPool2d(2)
        # fully connected layer(nn.Linear) 객체 fc 선언 (입력크기 : 20x4x4 = 1408 ,출력크기 : 10)
        self.fc = nn.Linear(1408, 10)

    def forward(self, x):
      # 입력 이미지의 크기를 계산하여 변수 in_size에 저장
        in_size = x.size(0)
        # conv1을 이용하여 x를 convolution 연산
        x = F.relu(self.mp(self.conv1(x)))
        # incept1을 이용하여 x를 Inception 모듈로 전달
        x = self.incept1(x)
        # conv2를 이용하여 x를 convolution 연산
        x = F.relu(self.mp(self.conv2(x)))
        # incept2을 이용하여 x를 Inception 모듈로 전달
        x = self.incept2(x)
        # x를 2차원 텐서(in_sizex-1)로 펼침
        x = x.view(in_size, -1)
        x = self.fc(x)
        # log_softmax 함수를 이용하여 모델
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
                100. * batch_idx / len(train_loader), loss.data[0]))


def test():
  # 학습한 모델 평가 모드로 전환
    model.eval()
    test_loss = 0
  # 테스트 데이터셋의 총 손실 값을 0으로 초기화
    correct = 0
  # 예측이 맞은 데이터 개수를 0으로 초기화
    for data, target in test_loader:
  # 테스트 데이터셋에서 데이터와 라벨을 하나씩 가져옴
        data, target = Variable(data, volatile=True), Variable(target)
   # 입력 데이터와 라벨을 Variable 객체로 만
        output = model(data)
    # 모델에 입력 데이터를 전달하여 출력값을 계산
        # sum up batch loss
        test_loss += F.nll_loss(output, target, size_average=False).data[0]
        # 현재 배치의 손실 값을 전체 테스트 데이터셋의 손실 값에 더
        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1]
        # 예측된 라벨 값(가장 큰 값)의 인덱스를 가져
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()
# 정답과 예측값을 비교하여 예측이 맞은 데이터의 개수를 세고, correct 변수에 더함
    test_loss /= len(test_loader.dataset)
  # 평균값 
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 10):
    train(epoch)
    test()
