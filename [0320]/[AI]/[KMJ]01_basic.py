# import는 기본적인 함수외의 다른 여러가지 함수들을 사용하기 위해 필요한 라이브러리를 불러온다는 의미이다.
# as @@은 앞에 언급된 라이브러리를 사용할 때 앞으로 @@으로 줄여서 부른다는 의미이다.
import numpy as np
# numpy : 수치해석, 통계 관련 기능을 구현하는 라이브러리
import matplotlib.pyplot as plt
# matplotlib.pyplot : 그래프를 그릴 때 사용하는 라이브러리

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]


# our model for the forward pass
def forward(x):
    return x * w


# Loss function
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)

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

# Plot it all
plt.plot(w_list, mse_list)
plt.ylabel('Loss')
plt.xlabel('w')
plt.show()
