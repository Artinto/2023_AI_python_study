from torch import nn # neural network 설치
import torch # Pytorch 설치
from torch import tensor # 다차원 행렬 연산 가능

x_data = tensor([[1.0], [2.0], [3.0]])
y_data = tensor([[2.0], [4.0], [6.0]])


class Model(nn.Module): # nn.Module에서 추적하는 데이터들을 모아 모델의 구조를 저장하여 상속
    def __init__(self): # nn.Module의 데이터들을 토대로 계층 변환을 정의
        super(Model, self).__init__() # __init__()은 변환을 위한 메소드
        self.linear = torch.nn.Linear(1, 1)  # One in and one out

    def forward(self, x):
        y_pred = self.linear(x) # Linear()을 통해 x데이터를 넣어 예측값을 연산한 후 y_pred에 저장
        return y_pred


model = Model()

criterion = torch.nn.MSELoss(reduction='sum') # 모든 데이터의 MSE계산
optimizer = torch.optim.SGD(model.parameters(), lr=0.01) # 확률적 경사하강법 옵티마이저로 각 단계의 w을 업데이트하고 lr로 w를 얼마나 빨리 업데이트할지 결정

for epoch in range(500):
    y_pred = model(x_data)

    loss = criterion(y_pred, y_data)
    print(f'Epoch: {epoch} | Loss: {loss.item()} ')

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


hour_var = tensor([[4.0]])
y_pred = model(hour_var)
print("Prediction (after training)",  4, model(hour_var).data[0][0].item())
