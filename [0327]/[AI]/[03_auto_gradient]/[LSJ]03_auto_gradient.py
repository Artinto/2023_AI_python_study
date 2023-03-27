import torch
import pdb

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
w = torch.tensor([1.0], requires_grad=True)
#데이터 셋 설정, 값이 1.0인 스칼라 텐서 w 설정,  w 텐서에 대한 기울기 저장 선언

# our model forward pass
def forward(x):
    return x * w

# Loss function
def loss(y_pred, y_val):
    return (y_pred - y_val) ** 2

# Before training
print("Prediction (before training)",  4, forward(4).item())

# Training loop
for epoch in range(10):
    for x_val, y_val in zip(x_data, y_data):
        y_pred = forward(x_val) # 1) Forward pass
        l = loss(y_pred, y_val) # 2) Compute loss
        l.backward() # 3) Back propagation to update weights 역전파를 통한 기울기 계산
        print("\tgrad: ", x_val, y_val, w.grad.item())
        w.data = w.data - 0.01 * w.grad.item()
        #item() : 딕셔너리에 있는 키와 값들의 쌍을 얻게 해주는 함수
        # Manually zero the gradients after updating weights
        w.grad.data.zero_()

    print(f"Epoch: {epoch} | Loss: {l.item()}")

# After training
print("Prediction (after training)",  4, forward(4).item())
