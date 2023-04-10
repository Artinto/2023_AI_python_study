rom torch import nn, optim, from_numpy
import numpy as np
# numpy를 np로써 import 해온다

xy = np.loadtxt('./data/diabetes.csv.gz', delimiter=',', dtype=np.float32)
# csv파일을 받아 ,기준으로 실수 형태로 받아오고 그 txt를 xy에 저장
x_data = from_numpy(xy[:, 0:-1])
# 마지막 열을 제외한 모든 데이터 가져옴
y_data = from_numpy(xy[:, [-1]])
# 마지막 열의 데이터만 가져옴
print(f'X\'s shape: {x_data.shape} | Y\'s shape: {y_data.shape}')
# 각각의 저장된 data의 형태 출력

class Model(nn.Module):
# nn.Module을 이용한 Model class 선언
    def __init__(self):
# 3개의 선형 층으로 구성 (8입력->1출력)
        super(Model, self).__init__()
        self.l1 = nn.Linear(8, 6)
# 첫번째 층 : 입력크기 8 -> 출력크기 6
        self.l2 = nn.Linear(6, 4)
# 두번째 층 : 입력크기 6 -> 출력크기 4
        self.l3 = nn.Linear(4, 1)
# 세번째 층 : 입력크기 4 -> 출력크기 1
        self.sigmoid = nn.Sigmoid()
# sigmoid 함수 설정
    def forward(self, x):
# forward 함수 설정
        out1 = self.sigmoid(self.l1(x))
# 입력 데이터 x가 첫번째 층을 통과한 결과를 out1에 저장
        out2 = self.sigmoid(self.l2(out1))
# out1은 두번째 층을 통과한 결과를 out2에 저장
        y_pred = self.sigmoid(self.l3(out2))
# out2는 마지막 층을 통과한 결과를 y_pred에 저장
        return y_pred
# y_pred는 최종 출력값

model = Model()
# Model 함수 정의

criterion = nn.BCELoss(reduction='mean')
# 오차 계산할 때 손실함수 BCELoss를 사용 -> 이진 분류로 사용
# reduction='mean'을 통해 평균 손실 계산
optimizer = optim.SGD(model.parameters(), lr=0.1)
# learning rate를 0.1로 맞추고 optimizer 설정

for epoch in range(100):
# 100번 반복(학습)
    y_pred = model(x_data)
# model 함수에 x_data를 넣은 결과 값을 y_pred에 저장
    loss = criterion(y_pred, y_data)
# 예측값과 실제값 사이의 계산된 criterion값을 loss에 저장
    print(f'Epoch: {epoch + 1}/100 | Loss: {loss.item():.4f}')
# Epoch의 값과 Loss 값 출력
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
