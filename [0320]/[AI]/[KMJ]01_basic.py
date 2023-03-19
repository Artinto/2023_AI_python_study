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
    # x(입력값)*w(가중치)의 값을 반환 : y_pred(예측한 출력값)형식으로 

    
    

# 손실합수 정의
# Loss function : 오차를 계산하는 함수(손실함수)

def loss(x, y):
# loss function을 정의하는 장소
    y_pred = forward(x)
    # x*w를 통해 계산한 예측값
    return (y_pred - y) * (y_pred - y)
    # loss(예측값-정답)^2값 반환



    
# 가중치와 오차들 찾기
# List of weights/Mean square Error (Mse) for each input

w_list = []
# weight(가중치)들을 모아 놓은 리스트
mse_list = []
# 오차값들을 모아 놓은 리스트

# 가중치 값 기계산하기
for w in np.arange(0.0, 4.1, 0.1):
# 0.0에서 4.1전까지 w값을 0.1씩 증가시키면서 반복
# 0.0  0.1  0.2  0.3  ...  3.8  3.9  4.0
    print("w=", w)
    # w=@ 형태로 w 값 출력
    l_sum = 0
    # l_sum : loss((예측값-정답)^2)들의 합
    
    for x_val, y_val in zip(x_data, y_data):
    # x_val에 x_data들을(1.0 2.0 3.0), y_val에 y_data들(2.0 4.0 6.0)을 묶어서 대입
        y_pred_val = forward(x_val)
        # x_val 데이터를 forword 함수에 넣은 값 : 예측값
        # y_pred_val = x_val * w
        l = loss(x_val, y_val)
        # x_val과 y_val를 이용하여 loss 계산 : 오차값 계산
        # l = (y_pred_val - y) * (y_pred_val - y)
        l_sum += l
        # l_sum에 구한 l을 계속 더하기
        
        print("\t", x_val, y_val, y_pred_val, l)
        # x_val, y_val, y_pred_val, l 프린트하기
        # \t은 들여쓰기해서 출력
        # 보기 쉽게 정리하기 위해 \t 사용
    # Now compute the Mean squared error (mse) of each
    # Aggregate the weight/mse from this run
    # MSE는 Mean squared error(평균제곱오차) 오차의 제곱 최솟값을 구하면서 weight를 찾아가는 방식
    print("MSE=", l_sum / len(x_data))
    # l_sum / len(x_data) : x_data의 크기로 l_sum을 나누기 => 평균 구하기
    
    # 출력 예시
    # w= 0.0
	#    1.0 2.0 0.0 4.0
	#    2.0 4.0 0.0 16.0
	#    3.0 6.0 0.0 36.0
    # MSE= 18.666666666666668
    # w= 0.1
	#    1.0 2.0 0.1 3.61
	#    2.0 4.0 0.2 14.44
	#    3.0 6.0 0.30000000000000004 32.49
    # MSE= 16.846666666666668
    # w= 0.2
	#    1.0 2.0 0.2 3.24
	#    2.0 4.0 0.4 12.96
	#    3.0 6.0 0.6000000000000001 29.160000000000004
    # MSE= 15.120000000000003
    
    
    w_list.append(w)
    # w_list에 w 추가
    mse_list.append(l_sum / len(x_data))
    # mse_list에 평균 추가



    
# 그래프 생성
# Plot it all
plt.plot(w_list, mse_list)
# w_list와 mse_list를 이용해서 그래프 그리기
plt.ylabel('Loss')
# y축의 레이블을 'Loss'라고 지정
plt.xlabel('w')
# x축의 레이블을 'w'라고 지정
plt.show()
# 불러오기
