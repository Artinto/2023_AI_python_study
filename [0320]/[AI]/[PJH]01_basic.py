import numpy as np # numpy라는 라이브러리를 np라는 이름으로 가져온다. numpy는 배열 객체와 배열 처리를 위한 함수를 제공
import matplotlib.pyplot as plt # Matplotlib 라이브러리에서 pyplot 모듈을 불러오는 코드이다. 다양한 그래프를 그리는 함수를 제공

x_data = [1.0, 2.0, 3.0] # list를 정의하고 1.0, 2.0, 3.0 이 세가지 수들을 저장하여 x_data에 할당
y_data = [2.0, 4.0, 6.0] # list를 정의하고 2.0, 4.0, 6.0 이 세가지 수들을 저장하여 y_data에 할당


# our model for the forward pass
def forward(x): # forward라는 이름은 x라는 인자를 받는 함수 정의
    return x * w # x를 입력받아 w와 곱하여 함수의 값을 반환


# Loss function
def loss(x, y): # loss라는 이름으로 x, y의 인자를 사용하는 함수 생성
    y_pred = forward(x) # 입력받은 x인자를 forward함수에 넣어 불어옴으로써 y_pred에 저장
    return (y_pred - y) * (y_pred - y) # 예측값 y_pred와 실제값 y의 차이를 계산 후 제곱한 값을 반환

# List of weights/Mean square Error (Mse) for each input
w_list = [] # 빈 리스트 w_list 정의
mse_list = [] # 빈 리스트 mse_list 정의

for w in np.arange(0.0, 4.1, 0.1): # w의 가중치를 0.0에서 4.0까지 0.1씩 올리며 반복
    # Print the weights and initialize the lost
    print("w=", w) # 위의 반복문이 돌아갈 때마다의 가중치를 출력
    l_sum = 0 # 내부의 for문에서 발생된 l_sum의 값들을 저장할 공간 생성과 동시에 외부 for문이 실행될 때 초기화

    for x_val, y_val in zip(x_data, y_data): # x_data배열과 y_data배열 요소들을 묶어 새로운 이터레이터를 생성, 그 새로운 이터레이터에 맞춰 각 순서의 값들을 x_val, y_val에 각각 지정하여 for문 실행
        # For each input and output, calculate y_hat
        # Compute the total loss and add to the total error
        y_pred_val = forward(x_val) # forward함수를 통해 x_val과 가중치 w를 곱한 y의 예측값을 y_pred_val에 저장
        l = loss(x_val, y_val) # loss를 불러와 예측값y와 실제값 y의 차이의 제곱을 l에 저장
        l_sum += l # 내부 반복문이 진행되면서 나온 l의 전체값을 저장
        print("\t", x_val, y_val, y_pred_val, l) # 각 인자의 값을 출력
    # Now compute the Mean squared error (mse) of each
    # Aggregate the weight/mse from this run
    print("MSE=", l_sum / len(x_data)) # 내부 for문이 끝날때마다 MSE, 즉 내부 for문에서 발생한 예측값 y와 실제값 y의 차이의 제곱 총합에 x_data 배열의 수를 나누어 출력, 즉 x_data와 w를 이용한 예측값 y와 실제값y의 차이에 대한 평균
    w_list.append(w) # w의 값을 그래프의 x축 지정
    mse_list.append(l_sum / len(x_data)) # w에 대한 예측값과 실제값의 차이를 y축 지정

# Plot it all
plt.plot(w_list, mse_list)
plt.ylabel('Loss')
plt.xlabel('w')
plt.show()
