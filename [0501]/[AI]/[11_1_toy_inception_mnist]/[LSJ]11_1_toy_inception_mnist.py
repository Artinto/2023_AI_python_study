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
batch_size = 64 # 학습할 데이터 크기 설정

# MNIST Dataset
train_dataset = datasets.MNIST(root='./data/', # 데이터 세트를 저장할 경로 지정
                               train=True, # 데이트 세트를 학습용으로 지정
                               transform=transforms.ToTensor(), # 데이터 세트의 형태를 Tensor 형태로 지정
                               download=True) # 현재 다운받아진 데이터 세트가 없다면 다운로드, 있다면 패스

test_dataset = datasets.MNIST(root='./data/',
                              train=False, # 데이터 세트를 테스트 용으로 지정
                              transform=transforms.ToTensor()) 

# Data Loader (Input Pipeline)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, 
                                           batch_size=batch_size,
                                           shuffle=True) # overfitting 방지를 위해 셔플줌해줌

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)


class InceptionA(nn.Module):

    def __init__(self, in_channels):
        super(InceptionA, self).__init__()
        self.branch1x1 = nn.Conv2d(in_channels, 16, kernel_size=1) # 입력: in_channels 출력 : 16인 1x1 convoultion

        self.branch5x5_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch5x5_2 = nn.Conv2d(16, 24, kernel_size=5, padding=2)

        self.branch3x3dbl_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch3x3dbl_2 = nn.Conv2d(16, 24, kernel_size=3, padding=1) # 입력 : 16, 출력 : 24, 3x3 convolution
        self.branch3x3dbl_3 = nn.Conv2d(24, 24, kernel_size=3, padding=1)

        self.branch_pool = nn.Conv2d(in_channels, 24, kernel_size=1)

    def forward(self, x):
        branch1x1 = self.branch1x1(x)

        branch5x5 = self.branch5x5_1(x)
        branch5x5 = self.branch5x5_2(branch5x5)

        branch3x3dbl = self.branch3x3dbl_1(x)
        branch3x3dbl = self.branch3x3dbl_2(branch3x3dbl)
        branch3x3dbl = self.branch3x3dbl_3(branch3x3dbl)

        branch_pool = F.avg_pool2d(x, kernel_size=3, stride=1, padding=1) # pooling 3x3, padding 1, stride 1
        branch_pool = self.branch_pool(branch_pool)

        outputs = [branch1x1, branch5x5, branch3x3dbl, branch_pool]
        return torch.cat(outputs, 1) # 축의 방향 : 1


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) #입력 1 출력 10 필터 5x5
        self.conv2 = nn.Conv2d(88, 20, kernel_size=5) #입력 88 출력 20 필터 5x5

        self.incept1 = InceptionA(in_channels=10) # 첫번째 인셉션으로 in_channel=10 지정
        self.incept2 = InceptionA(in_channels=20) # 두번째 인셉션으로 in_channe=20 지정

        self.mp = nn.MaxPool2d(2) #MaxPooling 진행
        self.fc = nn.Linear(1408, 10) #입력 1408, 출력 10

    def forward(self, x):
        in_size = x.size(0) # 배치 사이즈 지정
        x = F.relu(self.mp(self.conv1(x))) # self.con1(x) maxpooling 진행 후 활성화 함수 적용
        x = self.incept1(x)
        x = F.relu(self.mp(self.conv2(x)))
        x = self.incept2(x)
        x = x.view(in_size, -1)  # flatten the tensor
        x = self.fc(x) # 입력 : 1408 출력 : 10
        return F.log_softmax(x) #softmax 이후 log값을 취함


model = Net() # 모델 선언

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


def train(epoch):
    model.train() # 학습모드
    for batch_idx, (data, target) in enumerate(train_loader): #enumerate : 인덱스와 원소를 동시에 접근할 수 있는 내장함수
        data, target = Variable(data), Variable(target)
        optimizer.zero_grad() 
        output = model(data) #출력값
        loss = F.nll_loss(output, target) # -log(y_t)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0: #batch 10번째마다 아래 내용 출력
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.data[0]))


def test(): 
    model.eval() # 평가모드
    test_loss = 0 # loss값 초기화
    correct = 0 # correct값 초기화
    for data, target in test_loader:
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data) #출력값
        # sum up batch loss
        test_loss += F.nll_loss(output, target, size_average=False).data[0] # 오차값 누적
        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum() #correct 값 누적

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 10): 총 9번 반복
    train(epoch)
    test()
