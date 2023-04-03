from torch import nn
import torch
from torch import tensor

x_data = tensor([[1.0], [2.0], [3.0]])
y_data = tensor([[2.0], [4.0], [6.0]])

class Model(nn.Module):
    def __init__(self):

        super(Model, self).__init__()
        #nn.Module 클래스를 상속받아 초기화 함수 __init__()을 호출
        self.linear = torch.nn.Linear(1, 1)  # One in and one out
        #linear 객체 생성 후 nn.Linear(1,1)를 통해 입력 데이터와 출력데이터를 1차원으로 정의

    def forward(self, x):
        #forward 함수 생성
        y_pred = self.linear(x)
        #위에서 정의한 linear함수에 x를 대입하여 y_pred 호출
        return y_pred
        #pred값 반환
model = Model()
#위에서 선언한 model클래스 객체 생성
criterion = torch.nn.MSELoss(reduction='sum')
#torch 모듈의 MSELoss 함수를 통해 Mean square error를 구함 (정답값과 예측값의 차이를 제곱한 후 평균한 값)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
# 경사하강법 함수로 이를 통해 gradient를 구하는 함수 optimizer를 생성 learning rate=0.01로 설정
for epoch in range(500):
    #학습 500번 수행
    y_pred = model(x_data)
    #위에서 선언한 model객체에서 forward함수에 x_data삽입
    loss = criterion(y_pred, y_data)
    #예측한 y_pred값과 정답값 y_data를 통해 MSE값을 구함
    print(f'Epoch: {epoch} | Loss: {loss.item()} ')
    # 학습할 때 마다 반복 횟수와 loss값 출력
    optimizer.zero_grad()
    # 학습을 수행하면서 앞서 계산한 gradient를 초기화
    loss.backward()
    # 역방향 전파를 수행하는 함수로 loss대한 gradient 계산
    optimizer.step()
    # 위에서 구한 gradient를 기준으로 가중치와 편향 값을 조정


# After training
hour_var = tensor([[4.0]])
#hour_var 에 4.0 값을 tensor형태로 저장
y_pred = model(hour_var)
# 위에서 선언한 hour_var를 학습한 모델에 적용하여 예측값을 구함
print("Prediction (after training)",  4, model(hour_var).data[0][0].item())
# 계산된 예측값 출력
