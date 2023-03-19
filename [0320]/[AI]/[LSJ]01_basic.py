import numpy as np # numpy를 np로 적어도 적용, Numpy: 수치 계산을 위해 효율적인 구현 기능을 제공해주는 패키지
import matplotlib.pyplot as plt #데이터를 그래프화 해주는 모듈인 matplotlib.pyplot을 plt로 대체

x_data = [1.0, 2.0, 3.0] # x(변수)에 들어갈 값들 설정
y_data = [2.0, 4.0, 6.0] # y(결과값)에 들어갈 값들 설정


# our model for the forward pass 순전파의 방식으로 계산
def forward(x): # forward(x)라는 x로 이루어진 함수 정의
    return x * w # 함수의 값을 x*w로 설정 후 반환


# Loss function # 오차 구하는 함수
def loss(x, y): # loss(x,y)라는 x,y로 이루어진 함수 정의
    y_pred = forward(x) # y의 예측값을 y_pred로 설정하며 그 값은 x*w로 구해짐
    return (y_pred - y) * (y_pred - y) # loss(x,y)의 값을 (y_pred - y)^2로 구해짐

# List of weights/Mean square Error (Mse) for each input
w_list = [] # w(x에 곱해질 가중치값)들을 설정해줄 리스트 생성
mse_list = [] #MSE, loss function을 통해 구해진 오차^2의 평균을 나타내는 리스트 생성

for w in np.arange(0.0, 4.1, 0.1): # w를 0.0부터 4.0까지 0.1씩 올라가며 반복
    # Print the weights and initialize the lost
    print("w=", w) # w=를 출력하고 그 옆에 w값 또한 출력
    l_sum = 0 # loss들의 합을 0으로 초기화

    for x_val, y_val in zip(x_data, y_data): # for 와 zip 내장함수를 통해 x_data,y_data 리스트의 원소들을 튜플의 형태로 반복 
        # For each input and output, calculate y_hat
        # Compute the total loss and add to the total error
        y_pred_val = forward(x_val)
        l = loss(x_val, y_val)
        # 위의 함수 정의에서와 같이 y의 예측값과 오차를 계산
        l_sum += l #반복을 통해 구해진 l값들을 더함
        print("\t", x_val, y_val, y_pred_val, l) # 구분하기 쉽게 탭을 통해 반복분마다 들여쓰기 함
    # Now compute the Mean squared error (mse) of each
    # Aggregate the weight/mse from this run
    print("MSE=", l_sum / len(x_data)) # MSE=오차의합/x값 개수(x_data의 길이)로 출력
    w_list.append(w) # w_list에 w 값들을 추가
    mse_list.append(l_sum / len(x_data)) #mse_list에 l_sum/len(x_data)값들을 추가

# Plot it all
plt.plot(w_list, mse_list) # w_list, mse_list를 x,y 축으로 하여 그래프 제작
plt.ylabel('Loss') # y축의 이름을 Loss로 설정
plt.xlabel('w') # x축의 이름을 w로 설정
plt.show() # 그래프 제작
