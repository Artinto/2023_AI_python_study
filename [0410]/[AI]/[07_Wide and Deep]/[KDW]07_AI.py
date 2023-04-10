from torch import nn, optim, from_numpy
import numpy as np

xy = np.loadtxt('./data/diabetes.csv.gz', delimiter=',', dtype=np.float32)
# csv파일을 다운로드 받아 읽어들이고 ,기준으로 실수형태로 가져온다.
x_data = from_numpy(xy[:, 0:-1])
# 마지막 열을 제외한 모든 데이터를 x데이터로 가져온다.
y_data = from_numpy(xy[:, [-1]])
# 마지막 열을 y데이터로 가져온다.
print(f'X\'s shape: {x_data.shape} | Y\'s shape: {y_data.shape}')
# data shape 출력

class Model(nn.Module):
# nn.Module를 상속받아와 Model class 선언
    def __init__(self):
        super(Model, self).__init__()
        self.l1 = nn.Linear(8, 6)
        #입력 dim을 8 out dim을 6으로 설정
        self.l2 = nn.Linear(6, 4)
        #앞서 6으로 설정한 out dim을 사용하여 입력 dim을 6으로 받고 out dim을 4로 설정
        self.l3 = nn.Linear(4, 1)
        #여러번의 linear함수를 거쳐 더욱 더 deep한 신경망으로 구성한다. 손실 오차 등 더욱 더 정확한 값을 출력하지만 시간이 오래걸린다. 몇번의 linear거치든 상관없지만
        #처음 입력 dim은 xdata열과 같아야하고 마지막 out dim도 마찬가지로 ydata 열의 수와 같아야한다.
        self.sigmoid = nn.Sigmoid()
        # sigmoid 함수
    def forward(self, x):
        # forward 함수
        out1 = self.sigmoid(self.l1(x))
        #위 linear함수와 마찬가지로 여러번의 sigmoid함수를 거치면서 좀더 deep한 신경망을 구성한다.
        out2 = self.sigmoid(self.l2(out1))
        # out1을 sigmoid함수를 통해 out2에 반환
        y_pred = self.sigmoid(self.l3(out2))
        return y_pred

model = Model()
# Model 객체 생성

criterion = nn.BCELoss(reduction='mean')
# 오차 계산함수 BCELoss(이진 분류) 사용
# reduction='mean'평균 손실
optimizer = optim.SGD(model.parameters(), lr=0.1)
# learning rate 0.1의 경상하강법 함수를 optimizer로 설정

for epoch in range(100):
# 100번 반복(학습)
    y_pred = model(x_data)
    # y_pred 구함
    loss = criterion(y_pred, y_data)
    #criterion를 통해 loss구함
    print(f'Epoch: {epoch + 1}/100 | Loss: {loss.item():.4f}')
    # Epoch, Loss 값 출력
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
