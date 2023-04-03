from torch import tensor
from torch import nn
from torch import sigmoid
import torch.nn.functional as F
import torch.optim as optim

# Training data and ground truth
x_data = tensor([[1.0], [2.0], [3.0], [4.0]])
y_data = tensor([[0.], [0.], [1.], [1.]])


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        #nn.Module 클래스를 상속받아 초기화 함수 __init__()을 호출
        self.linear = nn.Linear(1, 1)  # One in and one out
        #linear 객체 생성 후 nn.Linear(1,1)를 통해 입력 데이터와 출력데이터를 1차원으로 정의
       
    def forward(self, x):

        y_pred = sigmoid(self.linear(x))
        #위에서 정의한 linear함수에 x를 대입한 후 반환값을 sigmoid함수에 대입하여 y_pred 값을 예측
        return y_pred
        #pred값 반환

# our model
model = Model()
#위에서 선언한 model클래스 객체 생성
criterion = nn.BCELoss(reduction='mean')
#BCE는 Binary cross-entropy의 약자로 logistic regression에서 loss를 구할 때 사용
#TRUE 나 FALSE와 같이 2개의 class로 구분하는 방식으로 0과 1사이의 값을 반환하며 1에 가까우면 true 0에 가까우면 false일 확률이 큰 것이다. 
optimizer = optim.SGD(model.parameters(), lr=0.01)
# 경사하강법 함수로 이를 통해 gradient를 구하는 함수 optimizer를 생성 learning rate=0.01로 설정 
for epoch in range(1000):
    #학습 1000번 수행
    y_pred = model(x_data)
    #위에서 선언한 model객체에서 forward함수에 x_data삽입
    loss = criterion(y_pred, y_data)
    #Binary cross-entropy함수에 예측한 y_pred값과 정답값 y_data를 대입하여 loss를 구함
    print(f'Epoch {epoch + 1}/1000 | Loss: {loss.item():.4f}')

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    # 학습을 수행하면서 앞서 계산한 gradient를 초기화
    loss.backward()
    # 역방향 전파를 수행하는 함수로 loss대한 gradient 계산
    optimizer.step()
    # 위에서 구한 gradient를 기준으로 가중치와 편향 값을 조정
    
# After training
print(f'\nLet\'s predict the hours need to score above 50%\n{"=" * 50}')
hour_var = model(tensor([[1.0]]))
print(f'Prediction after 1 hour of training: {hour_var.item():.4f} | Above 50%: {hour_var.item() > 0.5}')
#모델에 tensor 1.0 값을 넣어 계산하여 출력하고 값이 0.5가 넘으면 true 아니면 false를 출력
hour_var = model(tensor([[7.0]]))
print(f'Prediction after 7 hours of training: {hour_var.item():.4f} | Above 50%: { hour_var.item() > 0.5}')
#위와 값은 방법으로 tensor[7.0]에 대한 값을 출력
