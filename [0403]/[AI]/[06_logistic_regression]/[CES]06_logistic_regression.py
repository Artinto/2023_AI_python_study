from torch import tensor
from torch import nn
from torch import sigmoid
import torch.nn.functional as F
import torch.optim as optim

x_data = tensor([[1.0], [2.0], [3.0], [4.0]])
# 새로 정의한 tensor 값을 x_data에 넣어줌
y_data = tensor([[0.], [0.], [1.], [1.]])
# 새로 정의한 tensor 값을 y_data에 넣어줌

class Model(nn.Module):
  # nn.Module 클래스를 상속하여 Model 클래스 정의
    def __init__(self):
        super(Model, self).__init__()
       # 모델 초기화
        self.linear = nn.Linear(1, 1)
       # 입력 1 -> 출력 1
    def forward(self, x):
    # forward 함수 정의
        y_pred = sigmoid(self.linear(x))
      # x를 받아 선형 계층에 적용한 후 sigmoid 함수를 적용하여 이진 출력값 계산
        return y_pred
        # 결과 값인 y_pred 반환

model = Model()
# Model 함수에 대입한 값을 model에 넣어줌

criterion = nn.BCELoss(reduction='mean')
# BCELoss는 Binary Cross Entripy 손실함수를 계산하는 클래스 -> 평균 손실 반환
optimizer = optim.SGD(model.parameters(), lr=0.01)
# SGD를 통해 경사 하강법 구현 , lr은 0.01로 설정 -> 그렇게 구한 값을 optimizer로 설정
for epoch in range(1000):
  # for 반복문을 통해 1000번 반복
    y_pred = model(x_data)
    # sigmoid함수를 적용한 x_data를 넣은 결과값을 y_pred에 저장
    loss = criterion(y_pred, y_data)
    # BCE를 통해 구한 손실 값의 평균을 loss에 대입
    print(f'Epoch {epoch + 1}/1000 | Loss: {loss.item():.4f}')
    # Epoch와 손실값 출력
    optimizer.zero_grad()
    # 앞에 정의한 기울기 값 초기화
    loss.backward()
    # 기울기 값 계산
    optimizer.step()
    # 계산된 기울기 값을 바탕으로 모델의 가중치와 편향 값을 업데이트
print(f'\nLet\'s predict the hours need to score above 50%\n{"=" * 50}')
# 예측을 출력하기 전에 출력되는 문자열
hour_var = model(tensor([[1.0]]))
# 모델에 입력값으로 시간당 공부 시간이 1시간인 데이터를 넣어 출력값을 계산
print(f'Prediction after 1 hour of training: {hour_var.item():.4f} | Above 50%: {hour_var.item() > 0.5}')
hour_var = model(tensor([[7.0]]))
# 모델에 입력값으로 시간당 공부 시간이 7시간인 데이터를 넣어 출력값을 계산
print(f'Prediction after 7 hours of training: {hour_var.item():.4f} | Above 50%: { hour_var.item() > 0.5}')
