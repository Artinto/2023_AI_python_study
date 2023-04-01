from torch import tensor
from torch import nn
from torch import sigmoid # 선형곡선을 위한 sigmoid함수를 이용하기 위해 import
import torch.nn.functional as F # functional은 활성화함수, 손실함수를 제공하는데 이를 F로 지정하여 사용
import torch.optim as optim # 최적화 알고리즘을 제공하는 패키지로 확률적 경사하강법을 제공

x_data = tensor([[1.0], [2.0], [3.0], [4.0]])
y_data = tensor([[0.], [0.], [1.], [1.]])


class Model(nn.Module):
    def __init__(self):
        """
        In the constructor we instantiate nn.Linear module
        """
        super(Model, self).__init__()
        self.linear = nn.Linear(1, 1) 

    def forward(self, x):
        """
        In the forward function we accept a Variable of input data and we must return
        a Variable of output data.
        """
        y_pred = sigmoid(self.linear(x)) # linear을 이용하여 각각의 가중치와 편향 tensor을 생성하고 이를 sigmoid함수로 입력값을 0,1로 분류
        return y_pred


model = Model()

criterion = nn.BCELoss(reduction='mean') # MSE로는 Loss를 구하지 못하여 BCE를 사용하여 1일 때와 0일 때의 각각의 손실을 계한하고 'mean'으로 설정하여 샘플의 평균값으로 계산
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(1000): # 학습 횟수 설정
    y_pred = model(x_data)

    loss = criterion(y_pred, y_data)
    print(f'Epoch {epoch + 1}/1000 | Loss: {loss.item():.4f}')

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(f'\nLet\'s predict the hours need to score above 50%\n{"=" * 50}')
hour_var = model(tensor([[1.0]])) # model에서 반환되는 tensor를 학습시간으로 사용 즉, model에서 반환되는 tensor는 가중치 w를 의미
print(f'Prediction after 1 hour of training: {hour_var.item():.4f} | Above 50%: {hour_var.item() > 0.5}')
hour_var = model(tensor([[7.0]]))
print(f'Prediction after 7 hours of training: {hour_var.item():.4f} | Above 50%: { hour_var.item() > 0.5}')
