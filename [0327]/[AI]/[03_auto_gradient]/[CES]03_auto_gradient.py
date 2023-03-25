import torch
import pdb

x_data = [1.0, 2.0, 3.0] # 데이터를 x_data에 입력
y_data = [2.0, 4.0, 6.0] # 데이터를 y_data에 입력
w = torch.tensor([1.0], requires_grad=True) 
# w값 입력 -> requires_grad=True 는 autograd 에 모든 연산(operation)들을 추적해야 한다고 알려주는 역할

# linear 방정식 함수 정의
def forward(x):
    return x * w

# Loss 방정식 함수 정의
def loss(y_pred, y_val):
    return (y_pred - y_val) ** 2

# Before training ->  이해 x
print("Prediction (before training)",  4, forward(4).item())

# Training loop
for epoch in range(10):
    # epoch를 10번 반복시킴으로써 10번 학습
    for x_val, y_val in zip(x_data, y_data):
        y_pred = forward(x_val) # foward 함수에 대입한 결과 값ㅇ르 y_pred에 저장
        l = loss(y_pred, y_val) # loss 함수에 대입한 결과 값을 l에 저장
        l.backward() # backward를 통해 역방향으로 각각의 gradient 값을 찾는다
        print("\tgrad: ", x_val, y_val, w.grad.item()) 
        # x_val, y_val, backward를 통해 찾은 w.grad값을 출력
        w.data = w.data - 0.01 * w.grad.item()
        #  # learning_rate 값을 0.01로 지정하고 최소 w.data를 찾기 위해 w값을 0.01*기울기 값만큼 빼준다 -> 그 값을 w.data에 저장
        w.grad.data.zero_()
        #  업데이트 후 gradient 값을 0으로 초기화

    print(f"Epoch: {epoch} | Loss: {l.item()}")
    # 실행 횟수와 loss 값 출력

# After training
print("Prediction (after training)",  4, forward(4).item())
# 이해 x
