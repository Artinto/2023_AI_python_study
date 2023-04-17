# https://github.com/pytorch/examples/blob/master/mnist/main.py
from __future__ import print_function 
from torch import nn, optim, cuda # pytorch의 모듈
from torch.utils import data
from torchvision import datasets, transforms
import torch.nn.functional as F 
import time


# Training settings
batch_size = 64
device = 'cuda' if cuda.is_available() else 'cpu' # GPU 사용하기위한 코드 사용불가시 CPU사용
print(f'Training MNIST Model on {device}\n{"=" * 44}')

# 학습용 데이터
train_dataset = datasets.MNIST(root='./mnist_data/', # 데이터 저장 경로
                               train=True, # 데이터를 테스트용과 학습용으로 구분하는데 학습용으로 가져옴.
                               transform=transforms.ToTensor(),# 데이터 저장시 텐서형으로 전환
                               download=True) # 지정 경로에 데이터가 없으면 다운로드
# 테스트용 데이터
test_dataset = datasets.MNIST(root='./mnist_data/', # 데이터 저장 경로
                              train=False, # 테스트용으로 데이터 사용
                              transform=transforms.ToTensor()) #  데이터 저장시 텐서형으로 전환

# Data Loader (Input Pipeline)
train_loader = data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size, # 배치 크기를 지정 (64)
                                           shuffle=True)  # 데이터 순서를 섞어서 가져옴

test_loader = data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,# 
                                          shuffle=False)# 데이터 순서를 섞지 않고 가져옴

# 신경망 모델 정의
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.l1 = nn.Linear(784, 520)
        self.l2 = nn.Linear(520, 320)
        self.l3 = nn.Linear(320, 240)
        self.l4 = nn.Linear(240, 120)
        self.l5 = nn.Linear(120, 10)
# INPUT LAYER 와 OUTPUT LAYER 사이에 HIDDEN LAYER의 노드를 직접 지정해줄 수 있는데
# 첫번째 레이어에서 노드를 520개 두번째 320 ....로 생성
# 이미지 픽셀이 28*28이라 처음은 784개 이다

    def forward(self, x):
        x = x.view(-1, 784)  # X를 (?,784)형태로 생성 (-1은 지정하지 않음)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)
      #위에서 생성한 레이어를 활성화 함수를 통해 노드를 활성화 하는 것이다.


model = Net()
#위에 선언한 클래스를 통해 모델을 재정의 
model.to(device)# CPU OR GPU 사용할 디바이스 설정
criterion = nn.CrossEntropyLoss() # CrossEntropyLoss함수를 통해 COST계산
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)# 경사하강법 함수를 이용해 gradient 계산

# 학습 함수 정의
def train(epoch):
    model.train() # 학습용으로 모델 지정
    for batch_idx, (data, target) in enumerate(train_loader): # 위에서 지정한 로더를 통해 데이터 가져옴 배치단위(64)로 가져옴
        data, target = data.to(device), target.to(device) # 데이터와 레이블을 GPU로 전송
        optimizer.zero_grad() # gradient 초기화
        output = model(data) # 데이터를 모델에 적용하여 결과 저장
        loss = criterion(output, target) # cost 계산
        loss.backward() # 역전파 실행
        optimizer.step() # gradient 계산 후 업데이트
        if batch_idx % 10 == 0:
            # 10번째마다 배치 상태와 loss를 출력
            print('Train Epoch: {} | Batch Status: {}/{} ({:.0f}%) | Loss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))


# 테스트 함수 정의
def test():
    model.eval() # 평가모드로 지정
    test_loss = 0 # 손실데이터 초기화
    correct = 0 # 정확도데이터 초기화
    for data, target in test_loader: #  위에서 지정한 로더를 통해 데이터 가져옴 배치단위(64)로 가져옴
        data, target = data.to(device), target.to(device) # 데이터와 타겟(레이블)값을 cpu or gpu로 보냄
        output = model(data) # 데이터를 모델에 적용하여 결과 저장
        
        test_loss += criterion(output, target).item()
         # 테스트를 통해 구한 손실 값을 누적
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()
        # 테스트를 통해 구한 정확도 값을 누적
    test_loss /= len(test_loader.dataset) # 누적값을 크기로 나누어 평균값 구함
    # 데이터 손실과 정확도 출력
    print(f'===========================\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)} '
          f'({100. * correct / len(test_loader.dataset):.0f}%)')


if __name__ == '__main__':
    since = time.time() # 학습 시작 시간 저장
    for epoch in range(1, 10):
        epoch_start = time.time() #epoch 시작 시간 저장
        train(epoch) # 학습 시작
        m, s = divmod(time.time() - epoch_start, 60)
        # 현재시간에서 epoch시작 시간을 빼서 학습 시간 저장
        print(f'Training time: {m:.0f}m {s:.0f}s')
        test() # 테스트 실행
        m, s = divmod(time.time() - epoch_start, 60)
         # 현재시간에서 epoch시작 시간을 빼서 TEST 시간 저장
        print(f'Testing time: {m:.0f}m {s:.0f}s')
        
    m, s = divmod(time.time() - since, 60)#
    # 학습 및 테스트 총 걸린 시간 저장
    print(f'Total Time: {m:.0f}m {s:.0f}s\nModel was trained on {device}!')
