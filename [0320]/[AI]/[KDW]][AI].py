import numpy as np
# 수치 해석용 python 라이브러리이며 백터와 행렬을 사용하는 선형대수 계산에 주로 사용
import matplotlib.pyplot as plt
# 다양한 데이터를 많은 방법으로 도식화 할 수 있는 파이썬 라이브러리


x_data = [1.0, 2.0, 3.0]
# 출력을 예측하기 위해 입력되는 데이터 셋
y_data = [2.0, 4.0, 6.0]
# x_data를 참고하여 도출되는 출력 데이터 셋


# our model for the forward pass
def forward(x):
#forward함수 정의 x -> x_data
    return x * w
    # x_data를 x로 가지고 온 후 w의 값을 곱하여 반환하는 프로세스


# Loss function
def loss(x, y):
#loss함수 정의 x-> x_data , y -> y_data
    y_pred = forward(x)
    # y_pred : 위 forward함수에 x_data를 파라미터로 하여 리턴된 갓ㅂ 
    return (y_pred - y) * (y_pred - y)
    # y_pred에 y_data를 뺸 후 제곱한 값 리턴 
    
# List of weights/Mean square Error (Mse) for each input
w_list = []
# forward 함수에 사용되는 변수 인 w(가중치) 값을 모아놓은 리스트
mse_list = []
# 연산 후 결과값과의 오차값을 모아놓은 리스트

for w in np.arange(0.0, 4.1, 0.1):
#for반복문으로 초기값 0.0에서 4.1까지 0.1씩 증가시켜 반복
    # Print the weights and initialize the lost
    print("w=", w)
    # w값 실시간 출력
    l_sum = 0
    # l_sum값 초기화
    for x_val, y_val in zip(x_data, y_data):
    #x_data 배열 데이터와 y_data 배열 데이터 2개를 합쳐 튜플 형태로 반환해준다. ex) ( x_data, y_data )
    #x_data에 접근을 원할 시 x_val , y_data에 접근을 원할 시 y_val를 사용한다.
    #이를 사용하는 이유는 for 반복문 실행 시 x_data와 같은 순서인 y_data를 사용함으로써 
        # For each input and output, calculate y_hat
        # Compute the total loss and add to the total error
        y_pred_val = forward(x_val)
        # x_val값을 파라미터로 forward연산(x_val값과 w값을 곱) 후 y_pred_val에 반환
        
        l = loss(x_val, y_val)
        #loss 함수에 x_val, y_val를 파라미터로 연산 후 l에 반환
        
        l_sum += l
        # 반환되는 l값을 모두 합하여 l_sum에 저장
        print("\t", x_val, y_val, y_pred_val, l)
        # 사용되는 각 데이터들 출력
    # Now compute the Mean squared error (mse) of each
    # Aggregate the weight/mse from this run
    print("MSE=", l_sum / len(x_data))
    # l_sum을 x_data의 크기만큼 나누어 l값의 평균을 구함
    w_list.append(w)
    # w_list에 w 데이터 추가
    mse_list.append(l_sum / len(x_data))
    # mse_list에 평균값 추가
# Plot it all
plt.plot(w_list, mse_list)
# w_list, mse_list 데이터를 이용해 그래프 그림
plt.ylabel('Loss')
# y축 레이블 이름 Loss로 지정
plt.xlabel('w')
# x축 레이블 이름 w로 지정
plt.show()
# 위 그래프를 화면에 출력
