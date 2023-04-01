from torch import nn
# PyTorch 라이브러리에서 nn 모듈 import
import torch
from torch import tensor
# PyTorch 라이브러리에서 tensor 모듈을 import

x_data = tensor([[1.0], [2.0], [3.0]])
# tensor를 지정해준 후 x_data에 저장 (입력값)
y_data = tensor([[2.0], [4.0], [6.0]])
# tensor를 지정해 준 후 y_data에 저장 (실제 결과값)

class Model(nn.Module):
# Model class 선언
    def __init__(self):
    # 신경망 모델이 사용될 구성품등을 정의 및 초기화 하는 메소드
        super(Model, self).__init__()
        # nn.Module 클래스의 초기화 함수를 호출
        self.linear = torch.nn.Linear(1, 1)  
        # 입력 데이터의 차원을 1로, 출력 데이터의 차원을 1로 설정한 nn.linear 객체 생성
    def forward(self, x):
    # forward 함수 생성
        y_pred = self.linear(x)
        # self.linear에 x를 대입한 결과 값을 y_pred에 대입
        return y_pred
        # y_pred 값 반환

model = Model()
# 앞에 선언한 Model 클래스를 호출하여 model에 정의
criterion = torch.nn.MSELoss(reduction='sum')
# MSE는 실제값과 예측값의 차이를 제곱한 값의 평균
# nn.MSELoss함수를 통해 손실함수를 정의
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
# SGD를 통해 경사 하강법 구현 , lr은 0.01로 설정 -> 그렇게 구한 값을 optimizer로 설정

for epoch in range(500):
  # 500번 반복
    y_pred = model(x_data)
    # model의 결과 값을 y_pred에 대입

    loss = criterion(y_pred, y_data)
    # MSE를 통해 구한 손실 값을 loss에 대입
    print(f'Epoch: {epoch} | Loss: {loss.item()} ')
    # epoch 값과 loss값을 하나씩 출력
    optimizer.zero_grad()
    # 앞에서 계산된 기울기 값 초기화
    loss.backward()
    # 기울기 값 계산
    optimizer.step()
    # 계산된 기울기 값을 바탕으로 모델의 가중치와 편향 값을 업데이트

hour_var = tensor([[4.0]])
# hour_var 변수에 4.0이 Tensor 형태로 저장됨
y_pred = model(hour_var)
# 앞에 설정한 변수 값을 대입한 model 결과 값을 y_pred에 출력
print("Prediction (after training)",  4, model(hour_var).data[0][0].item())
# 계산된 예측값 출력
