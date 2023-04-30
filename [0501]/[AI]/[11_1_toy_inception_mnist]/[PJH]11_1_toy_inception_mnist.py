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
batch_size = 64

# MNIST Dataset
train_dataset = datasets.MNIST(root='./data/',
                               train=True,
                               transform=transforms.ToTensor(),
                               download=True)

test_dataset = datasets.MNIST(root='./data/',
                              train=False,
                              transform=transforms.ToTensor())

# Data Loader (Input Pipeline)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)

# 신경망 모델
class InceptionA(nn.Module):

    def __init__(self, in_channels):
        super(InceptionA, self).__init__()
        #분기 1 - 1x1 컨볼루션
        self.branch1x1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        #분기 2 - 3x3 컨볼루션
        self.branch5x5_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch5x5_2 = nn.Conv2d(16, 24, kernel_size=5, padding=2)
        #분기 3 - 4x4 컨볼루션
        self.branch3x3dbl_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch3x3dbl_2 = nn.Conv2d(16, 24, kernel_size=3, padding=1)
        self.branch3x3dbl_3 = nn.Conv2d(24, 24, kernel_size=3, padding=1)
        #분기 4 - 입력텐서 풀링
        self.branch_pool = nn.Conv2d(in_channels, 24, kernel_size=1)

    def forward(self, x):
        branch1x1 = self.branch1x1(x)

        branch5x5 = self.branch5x5_1(x)
        branch5x5 = self.branch5x5_2(branch5x5)

        branch3x3dbl = self.branch3x3dbl_1(x)
        branch3x3dbl = self.branch3x3dbl_2(branch3x3dbl)
        branch3x3dbl = self.branch3x3dbl_3(branch3x3dbl)

        branch_pool = F.avg_pool2d(x, kernel_size=3, stride=1, padding=1)
        branch_pool = self.branch_pool(branch_pool)
        #분기별 특성맵들을 채널차원을 기준으로 연결 후 출력생성
        outputs = [branch1x1, branch5x5, branch3x3dbl, branch_pool]
        #output을 1차원으로 결합
        return torch.cat(outputs, 1)

#모델 설정
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)#입력 채널 1개, 출력 채널 10개, 사이즈 5x5의 필터사용
        self.conv2 = nn.Conv2d(88, 20, kernel_size=5)#입력 채널 88개, 출력 채널 20개, 사이즈 5x5

        self.incept1 = InceptionA(in_channels=10)#위 InceptionA클래스를 통헤 10개의 입력채널을 받아 특징 맵을 통한 4개의 채널을 출력
        self.incept2 = InceptionA(in_channels=20)#위 InceptionA클래스를 통해 20개의 입력채널을 받아 특징 맵을 통한 4개의 채널을 출력

        self.mp = nn.MaxPool2d(2)#2x2 사이즈의 풀링 윈도우에서 각 위치에서의 최대값을 계산하여 입력 이미지의 크기를 줄인다.
        self.fc = nn.Linear(1408, 10)#feature를 1408차원을 받아 10차원으로 변환

    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x)))#입력 이미지 x에 self.conv1 컨볼루션 레이어를 적용하고, 그 결과에 self.mp 맥스 풀링 레이어를 적용한 뒤, 활성화 함수인 렐루 함수를 적용합니다.
        x = self.incept1(x)
        x = F.relu(self.mp(self.conv2(x)))
        x = self.incept2(x)
        x = x.view(in_size, -1)  # flatten the tensor
        x = self.fc(x)
        return F.log_softmax(x)


model = Net()

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item())) /파이썬 버전 문제로 인한 loss.data[0]에서 loss.item()으로 수정

def test():
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            # sum up batch loss
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            # get the index of the max log-probability
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 10):
    train(epoch)
    test()
