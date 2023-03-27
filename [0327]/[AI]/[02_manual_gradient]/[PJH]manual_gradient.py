# Training Data
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0  # a random guess: random value


# our model forward pass
def forward(x):
    return x * w


# Loss function
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)


# compute gradient
def gradient(x, y):  # d_loss/d_w
    return 2 * x * (x * w - y)
# gradient라는 함수는 앞서 설명했듯이 loss가 최소일 때의 w라는 가중치를 구하는 함수이다.


# Before training
print("Prediction (before training)",  4, forward(4)) # 학습 전의 w를 나타냄, 즉 학습 전의 학습량으로 정의

# Training loop
for epoch in range(10): # range()는 ()안의 만큼 for문을 돌리는 것으로 ()안의 숫자가 많아질 수록 loss=0에 수렴하는 가중치를 더 정확히 구할 수 있음
    for x_val, y_val in zip(x_data, y_data):
        # Compute derivative w.r.t to the learned weights
        # Update the weights
        # Compute the loss and print progress
        grad = gradient(x_val, y_val)
        w = w - 0.01 * grad # gradient의 리턴값인 w의 크기를 확인 후 크기에 따라 많이 움직일지 적게 움직일지를 퍼센트 즉 0.01을 입력하여 다음 반복 실행 때 쓸 수 있도록 저장해줌
        print("\tgrad: ", x_val, y_val, round(grad, 2))
        l = loss(x_val, y_val)
    print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))

# After training
print("Predicted score (after training)",  "4 hours of studying: ", forward(4)) # 학습 후 학습으로 인한 w의 증가량을 나타냄
