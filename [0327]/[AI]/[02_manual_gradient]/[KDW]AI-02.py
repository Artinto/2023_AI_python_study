
# Training Data
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
#x_data 셋, y_data 셋 구성

w = 1.0  # a random guess: random value
# 보통은 w(가중치)값을 랜덤생성하여 진행하지만 예제에서 1.0으로 지정


# our model forward pass
def forward(x):
    return x * w
# x 데이터와 w(가중치)를 곱해주는 선형 방정식 함수


# Loss function
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)
# loss 값을 계산해주는 함수 정의


# compute gradient
def gradient(x, y):  # d_loss/d_w
    return 2 * x * (x * w - y)
# 기울기 값 (gragient)를 계산하는 함수 정의 ( loss가 최소일 때 w가중치를 구하긴 위한 조정값을 구해주는 함수)


# Before training
print("Prediction (before training)",  4, forward(4))
#훈련 전 학습을 통해 foward예측값을 출력

# Training loop
for epoch in range(10):
    for x_val, y_val in zip(x_data, y_data):
        # Compute derivative w.r.t to the learned weights
        # Update the weights
        # Compute the loss and print progress
        grad = gradient(x_val, y_val)
        # loss가 최소인 가중치를 구하기 위해 grad를 구함
        w = w - 0.01 * grad
        # 위해선 구한 grad를 통해 loss가 최소인 w를 구함
        print("\tgrad: ", x_val, y_val, round(grad, 2))
        l = loss(x_val, y_val)
    print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))
  # epoch 학습 횟 수, 가중치, loss 값 출력
# After training
print("Predicted score (after training)",  "4 hours of studying: ", forward(4))
#학습 후 변경된 w가중치를 통한 예측값 출력
