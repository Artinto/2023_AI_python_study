#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torchvision.models as models

# GPU를 사용할 수 있는 환경이라면 GPU로 이동시켜 학습과 평가 수행
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# batch 사이즈 설정
batch_size = 64

# CIFAR10 데이터 로드
train_transform = transforms.Compose([ # 여러가지 transform함수를 이용하여 데이터의 다양성을 높여 더 일반화된 학습 가능
        transforms.RandomResizedCrop(32, scale=(0.8, 1.0)), # 입력된 이미지를 무작위로 잘라 원하는 크기로 조정(32*32, 0.8 <= 크기 <= 1.0)
        transforms.RandomHorizontalFlip(), # 이미지를 50% 확률로 좌우 반전시킴
        transforms.ToTensor(), # 이미지를 tensor형으로 변환
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), # 데이터의 평균과 표준편차를 이용하여 정규화, 성능향상, 수렴속도 향상
        transforms.RandomErasing(p=0.1, scale=(0.02, 0.33)) # 데이터를 일부러 지워 데이터 확장을 수행, 강인한 성능, p는 지우기 확률, scale은 이미지 크기 비율
    ])

test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

train_dataset = datasets.CIFAR10(root='./data', train=True, download=True,
                                 transform=train_transform)

test_dataset = datasets.CIFAR10(root='./data', train=False, download=True,
                                transform=test_transform)

# 데이터 로드 설정
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size, shuffle=True, num_workers=4, pin_memory=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size, shuffle=False, num_workers=4, pin_memory=True)

# 모델 구성
model = models.resnet18(num_classes=10).to(device) # ResNet18은 torchvision패키지에서 제공되는 이미지 인식 분야 신경망 아키텍쳐, 분류가 10개이므로 num_classes = 10, GPU에서 학습 할 수 있도록 함

# 손실 함수 및 optimizer 설정
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001, betas=(0.99, 0.999), weight_decay=5e-4) # betas=(이동평균,제곱된 그레디언트의 이동평균), weight_decay는 정규화로 인한 파라미터 값이 커지는 것을 방지
scheduler = lr_scheduler.MultiStepLR(optimizer, milestones=[80, 120], gamma=0.1) # epoch에 따라 학습률 조정, epoch가 80 ~ 120에서 학습률이 gamma비율만큼 감소, overfiting방지, 학습과정이 안정적

# 모델 학습
num_epochs = 160
total_batches = len(train_loader)
for epoch in range(num_epochs):
    train_loss, train_acc = 0.0, 0.0
    model.train()
    for i, (images, labels) in enumerate(train_loader):
        # CUDA로 데이터를 GPU로 옮기기
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1) # 예측값에서 가장 큰 값과 그에 해당하는 인덱스 저장
        train_acc += (predicted == labels).sum().item() # predicted와 labels를 비교하여 정확히 예측한 데이터의 수를 누적
        print('\rEpoch [{}/{}], Batch [{}/{}], Train Loss: {:.4f}, Train Accuracy: {:.2f}%'.format(epoch + 1, num_epochs, i+1, total_batches, train_loss/(i+1), 100*train_acc/((i+1)*train_loader.batch_size)), end='')
    scheduler.step()
    train_loss /= len(train_loader)
    train_acc /= len(train_loader.dataset)

    # 1 epoch 마다 loss와 accuracy 출력
    print('\rEpoch [{}/{}], Train Loss: {:.4f}, Train Accuracy: {:.2f}%'.format(epoch + 1, num_epochs, train_loss, train_acc * 100))

# 모델 평가
model.eval() # 모델을 평가 모드로 전환
with torch.no_grad():
    test_loss, test_acc = 0.0, 0.0
    for images, labels in test_loader:
        # CUDA로 데이터를 GPU로 옮기기
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        test_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        test_acc += (predicted == labels).sum().item()

    test_loss /= len(test_loader)
    test_acc /= len(test_loader.dataset)

    # 각 epoch에 따른 학습된 모델을 바탕으로 test한 결과 출력
    print('Test Loss: {:.4f}, Test Accuracy: {:.2f}%'
          .format(test_loss, test_acc*100))


