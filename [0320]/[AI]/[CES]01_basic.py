import numpy as np # numpy는 과학 계산을 위한 라이브러리로서 다차원 배열을 처리하는데 필요한 여러 유용한 기능을 제공하고 있다
import matplotlib.pyplot as plt # matplotlib.pyplot 모듈의 각각의 함수를 사용해서 간편하게 그래프를 만들고 변화를 줄 수 있다

x_data = [1.0, 2.0, 3.0] # list 선언하여 x_data에 할당
y_data = [2.0, 4.0, 6.0] # list 선언하여 y_data에 할당


# our model for the forward pass
def forward(x): # forward()함수 정의 -> 변수 x 설정
    return x * w # 입력받은 x와 w의 곱을 반환


# Loss function
def loss(x, y): # loss()함수 정의 -> 변수 x,y 설정
    y_pred = forward(x) # forward(x)의 결과 값을 y_pred에 저장
    return (y_pred - y) * (y_pred - y) # 저장한 값의 제곱을 반환

# List of weights/Mean square Error (Mse) for each input
w_list = [] # 빈 list를 W_list에 저장
mse_list = [] # 빈 list를 mse_list에 저장

for w in np.arange(0.0, 4.1, 0.1): # W를 0.0에서 4.1까지 0.1만큼 증가시키며 반복
    # Print the weights and initialize the lost
    print("w=", w) # 반복할때마다 증가된 W값 출력
    l_sum = 0 # l_sum값을 0으로 초기화

    for x_val, y_val in zip(x_data, y_data): 
    # zip 함수의 원리는 길이가 같은 두개 이상의 자료형에 대하여 동일한 위치의 자료끼리 튜플 형태로 묶어주는 역할을 수행
        # For each input and output, calculate y_hat
        # Compute the total loss and add to the total error
        y_pred_val = forward(x_val) # forward 함수에 x_val을 넣은 값을 y_pred_val에 저장
        l = loss(x_val, y_val) # loss함수에 변수 x_val 과 y_val을 넣은 값을 l에 저장
        l_sum += l # 반복될 때마다 l_sum에 1을 더함 (개수 count)
        print("\t", x_val, y_val, y_pred_val, l) # tab을 기준으로 x_val, y_val, y_pred_val, l 값 출력
    # Now compute the Mean squared error (mse) of each
    # Aggregate the weight/mse from this run
    print("MSE=", l_sum / len(x_data)) # l_sum을 x_data의 길이로 나눈 값을 출력
    w_list.append(w) # 앞에 선언한 w_list에 w값 추가
    mse_list.append(l_sum / len(x_data)) # 앞에 선언한 mse_list에 l_sum / len(x_data) 값 추가

# Plt.plot -> 각각의 축을 지정하여 그래프를 시각화해서 보여준다
plt.plot(w_list, mse_list) # plt.plot(x, y)
plt.ylabel('Loss') # plt.xlabel('X-Axis') -> x축
plt.xlabel('w') # plt.ylable('Y-Axis') -> y축
plt.show() # 그래프 보여주기
