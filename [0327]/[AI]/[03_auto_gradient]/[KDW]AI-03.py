import torch
import pdb
# 모듈 임포트

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
#데이터 셋 설정
w = torch.tensor([1.0], requires_grad=True)
# w값을 1.0으로 지정 , 기울기 값을 추적할 텐선를 선언할 때 requires_grad=True로 지정
# our model forward pass
def forward(x):
    return x * w
# 예측값 함수 
# Loss function
def loss(y_pred, y_val):
    return (y_pred - y_val) ** 2
# loss 값 구하는 함수
# Before training
print("Prediction (before training)",  4, forward(4).item())
# 훈련 전 예측값을 출력
# Training loop
for epoch in range(10):
# 훈련 횟수 10번 지정
    for x_val, y_val in zip(x_data, y_data):
        y_pred = forward(x_val) # 1) Forward pass
        # 예측값 y_pred에 저장
        l = loss(y_pred, y_val) # 2) Compute loss
        # 손실값 l에 저장
        l.backward() # 3) Back propagation to update weights
        # backward를 통해 역방향으로 gradient를 구함
        print("\tgrad: ", x_val, y_val, w.grad.item())
        w.data = w.data - 0.01 * w.grad.item() # 최적의 w를 구하기 위해 gradient값에 learning rate 0.01을 곱하여
        #가중치에서 빼며 가중치 값을 조정해 나간다.

        # Manually zero the gradients after updating weights
        w.grad.data.zero_()
        # gardient를 업데이트 후 초기화
    print(f"Epoch: {epoch} | Loss: {l.item()}")
    # 반복 횟수 와 loss 값 출력
# After training
print("Prediction (after training)",  4, forward(4).item())
# 훈련 후 예측 값 출력
