# 라이브러리 불러오기
# import는 기본적인 함수외의 다른 여러가지 함수들을 사용하기 위해 필요한 라이브러리를 불러온다.
# as @@은 앞에 언급된 라이브러리를 사용할 때 앞으로 @@으로 줄여서 부른다는 의미이다.

import numpy as np
# numpy : 수치해석, 통계 관련 기능을 구현하는 라이브러리
import matplotlib.pyplot as plt
# matplotlib.pyplot : 그래프를 그릴 때 사용하는 라이브러리




# 학습할 데이터 셋 구성

x_data = [1.0, 2.0, 3.0]
# x데이터 : 예측할 때 참고할 값(입력데이터)
y_data = [2.0, 4.0, 6.0]
# y데이터 : 예측 해야하는 데이터의 정답 값(출력데이터의 정답 값)




# 학습 모델 생성
# our model for the forward pass
# forword pass란 순전파를 의미하며, 모델이 입력층부터 시작되어 출력층까지 순서대로 변수를 저장, 계산한다는 것을 의미한다.
# 역전파는 출력층부터 입력층 방향으로 계산된다.

def forward(x):
# forward를 정의하는 장소
    return x * w
    # x(입력데이터)*w(가중치)의 값을 반환 : y_pred(예측한 출력데이터)

    
    


# 손실합수 정의
# Loss function : 오차를 계산하는 함수(손실함수)

def loss(x, y):
# loss function을 정의하는 장소
    y_pred = forward(x)
    # x*w를 통해 계산한 예측값
    return (y_pred - y) * (y_pred - y)
    # loss(예측값-정답)^2값 반환.



# 
# List of weights/Mean square Error (Mse) for each input

w_list = []
mse_list = []

for w in np.arange(0.0, 4.1, 0.1):
    # Print the weights and initialize the lost
    print("w=", w)
    l_sum = 0

    for x_val, y_val in zip(x_data, y_data):
        # For each input and output, calculate y_hat
        # Compute the total loss and add to the total error
        y_pred_val = forward(x_val)
        l = loss(x_val, y_val)
        l_sum += l
        print("\t", x_val, y_val, y_pred_val, l)
    # Now compute the Mean squared error (mse) of each
    # Aggregate the weight/mse from this run
    print("MSE=", l_sum / len(x_data))
    w_list.append(w)
    mse_list.append(l_sum / len(x_data))



    

# 그래프 생성
# Plot it all
plt.plot(w_list, mse_list)
plt.ylabel('Loss')
plt.xlabel('w')
plt.show()
