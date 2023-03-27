# Training Data
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
# 데이터 셋 설정

w = 1.0  # a random guess: random value
#랜덤 w가중치 설정. 1.0이 아니어도 됨

# our model forward pass
def forward(x):
    return x * w
  #forward(x)함수 , y= x*w 정의


# Loss function
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)
# loss(x,y) 함수, 오차=(y_pred - y)^2 정의


# compute gradient
def gradient(x, y):  # d_loss/d_w
    return 2 * x * (x * w - y)
# gradient(x, y) 함수, 오차의 기울기 = 2*x*(x*w-y) 정의


# Before training
print("Prediction (before training)",  4, forward(4))
# 훈련 전 4시간 공부 후 성적 예측값 출력

# Training loop
for epoch in range(10):
    for x_val, y_val in zip(x_data, y_data):
        # Compute derivative w.r.t to the learned weights
        # Update the weights
        # Compute the loss and print progress
        grad = gradient(x_val, y_val)
        w = w - 0.01 * grad
        print("\tgrad: ", x_val, y_val, round(grad, 2))
        l = loss(x_val, y_val)
    print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))
 # 10번의 epoch 동안 가장 정확도가 높은 w값 찾기 위해 각각의 값 출력

# After training
print("Predicted score (after training)",  "4 hours of studying: ", forward(4))
# 훈련 후 4시간 공부 후 성적 예측값 출력
