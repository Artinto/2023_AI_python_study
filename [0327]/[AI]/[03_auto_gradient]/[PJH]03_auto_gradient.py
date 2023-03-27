import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
w = torch.tensor([1.0], requires_grad=True)
# scalar(1.0)을 가진 tensor객체인 w를 생성하는 코드
# requires_grad=True는 w가 학습 가능한 변수로 사용됨을 의미
# 동시에 연산할때마다 w를 불러와야 하기때문에 수시로 불러올 수 있는 저장공간을 뜻함

# our model forward pass
def forward(x):
    return x * w # x와 w를 사용하여 y값을 예측

# Loss function
def loss(y_pred, y_val):
    return (y_pred - y_val) ** 2 #MSE손실

# Before training
print("Prediction (before training)",  4, forward(4).item())

# Training loop
for epoch in range(10):
    for x_val, y_val in zip(x_data, y_data):
        y_pred = forward(x_val) # 1) Forward pass
        l = loss(y_pred, y_val) # 2) Compute loss
        l.backward() # 3) # Back propagation의 이론을 바탕으로 gradient를 역방향으로 구하여 w.grad에 저장
        print("\tgrad: ", x_val, y_val, w.grad.item())
        w.data = w.data - 0.01 * w.grad.item() # w_data를 gradient에 learning late 0.01을 곱한 후 기존 w_data의 값에서 뺀값으로 갱신

        # Manually zero the gradients after updating weights
        w.grad.data.zero_() # 업데이트 후 gradient를 초기화

    print(f"Epoch: {epoch} | Loss: {l.item()}")

# After training
print("Prediction (after training)",  4, forward(4).item())
