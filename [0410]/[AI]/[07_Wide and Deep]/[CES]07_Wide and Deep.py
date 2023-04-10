rom torch import nn, optim, from_numpy
import numpy as np

xy = np.loadtxt('./data/diabetes.csv.gz', delimiter=',', dtype=np.float32)
# csv파일을 받아 ,기준으로 실수 형태로 받아오고 그 txt를 xy에 저장
x_data = from_numpy(xy[:, 0:-1])

y_data = from_numpy(xy[:, [-1]])

print(f'X\'s shape: {x_data.shape} | Y\'s shape: {y_data.shape}')


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

    def forward(self, x):
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
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(100):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(f'Epoch: {epoch + 1}/100 | Loss: {loss.item():.4f}')
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
