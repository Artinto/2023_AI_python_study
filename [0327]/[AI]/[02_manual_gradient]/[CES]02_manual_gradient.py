x_data = [1.0, 2.0, 3.0] 
# x_data 입력
y_data = [2.0, 4.0, 6.0] 
# y_data 입력

w = 1.0 
# 랜덤한 w값 입력


# linear 방정식 함수 정의
def forward(x):
    return x * w


# Loss 방정식 함수 정의
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)


# 기울기 값 (gragient) 계산 함수 정의
def gradient(x, y):  # d_loss/d_w
    return 2 * x * (x * w - y)

# 이해 안됨
print("Prediction (before training)",  4, forward(4))

# Training loop
for epoch in range(10): 
# epochfmf 10번 반복시킴으로써 10번 학습
    for x_val, y_val in zip(x_data, y_data): 
    # 각각에 맞는 데이터를 반복문을 통해 하나씩 입력
        grad = gradient(x_val, y_val)
        # gradient 함수에 대입한 결과 값을 grad에 저장
        w = w - 0.01 * grad
        # learning_rate 값을 0.01로 지정하고 최소 w를 찾기 위해 w값을 0.01*기울기 값만큼 빼준다 -> 그 값을 w에 저장
        print("\tgrad: ", x_val, y_val, round(grad, 2))
        # x_val, y_val, 소수 둘째자리까지 반올림한 grad 값 출력
        l = loss(x_val, y_val)
        # loss 함수에 대입한 결과 값을 l에 저장
    print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))
    # 학습한 횟수, 소수 둘째자리까지 반올림한 w값과, 소수 둘째자리까지 반올림한 l값 출력

# After training
print("Predicted score (after training)",  "4 hours of studying: ", forward(4))
# 이해 안됨
