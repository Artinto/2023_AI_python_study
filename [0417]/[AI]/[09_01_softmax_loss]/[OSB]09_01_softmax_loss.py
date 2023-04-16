from torch import nn, tensor, max
import numpy as np

# Cross entropy example
# One hot
# 0: 1 0 0
# 1: 0 1 0
# 2: 0 0 1

Y = np.array([1, 0, 0]) # one-encoding을 통해서 Y값이 세번째 중 0이라는 것을 알려줌
Y_pred1 = np.array([0.7, 0.2, 0.1]) # 예상값 1 - 실제값과 유사.
Y_pred2 = np.array([0.1, 0.3, 0.6]) # 예상값 2 - 실제값과 다름.
print(f'Loss1: {np.sum(-Y * np.log(Y_pred1)):.4f}')  # 예상값 1에 대해 Cross Entropy Loss에 대해서 계산하여 소수점 4자리까지 출력.
print(f'Loss2: {np.sum(-Y * np.log(Y_pred2)):.4f}')  # 예상값 2에 대해 Cross Entropy Loss에 대해서 계산하여 소수점 4자리까지 출력.

# Softmax + CrossEntropy (logSoftmax + NLLLoss)
loss = nn.CrossEntropyLoss() # Pytorch의 모듈을 이용해서 Cross Entropy Loss를 계산, 입력으로 확률분포를 나타내는 logit값(softmax 통과X)과 Y의 라벨을 받는다.

# target is of size nBatch
# each element in target has to have 0 <= value < nClasses (0-2)
# Input is class, not one-hot
Y = tensor([0], requires_grad=False)  # nn.CrossEntropyLoss()로 계산을 위해서 one-hot encoding 형식이 아닌 라벨 값을 Tensor로 선언.
                                      # 또한 requires_grad=False를 이용해 해당 Tensor에 대해 Autograd를 비활성화함.

# input is of size nBatch x nClasses = 1 x 4
# Y_pred are logits (not softmax)
Y_pred1 = tensor([[2.0, 1.0, 0.1]]) # 예상값 1 - logit형태로 실제값과 유사하게 선언
Y_pred2 = tensor([[0.5, 2.0, 0.3]]) # 예상값 2 - logit형태로 실제값과 다르게 선언.

l1 = loss(Y_pred1, Y)  # 예상값 1과 Y를 앞서 선언한 nn.CrossEntropyLoss에 대입해서 cross entropy loss를 계산한다
l2 = loss(Y_pred2, Y)  # 예상값 2와 Y를 앞서 선언한 nn.CrossEntropyLoss에 대입해서 cross entropy loss를 계산한다

# 계산한 오차 출력 및 logit 형태로 선언된 예상값(1,2)의 라벩 값을 출력
print(f'PyTorch Loss1: {l1.item():.4f} \nPyTorch Loss2: {l2.item():.4f}')
print(f'Y_pred1: {max(Y_pred1.data, 1)[1].item()}')
print(f'Y_pred2: {max(Y_pred2.data, 1)[1].item()}')

# target is of size nBatch
# each element in target has to have 0 <= value < nClasses (0-2)
# Input is class, not one-hot
Y = tensor([2, 0, 1], requires_grad=False) # Line 22와는 다르게 라벨로 선언하되 Batch 단위로 선언.-> 3 label, Autograd 비활성화.

# input is of size nBatch x nClasses = 2 x 4
# Y_pred are logits (not softmax)
# line 27,28과 다르게 라벨의 3개이므로 예상값을 3x3의 배열 의 형태로 선언함.(하나의 행당 하나의 라벨을 담당함)
Y_pred1 = tensor([[0.1, 0.2, 0.9], # Y가 2, 0, 1이므로 Y값과 유사하게 선언.
                  [1.1, 0.1, 0.2],
                  [0.2, 2.1, 0.1]])

Y_pred2 = tensor([[0.8, 0.2, 0.3], # Y와 다르게 선언.
                  [0.2, 0.3, 0.5],
                  [0.2, 0.2, 0.5]])
# Batch 단위의 Y와 예상값들의 Cross Entropy Loss 계산
l1 = loss(Y_pred1, Y) 
l2 = loss(Y_pred2, Y)
# 계산한 Cross Entropy Loss값 출력 .item을 통해 Tensor로 반환된 결과에서 값만 뽑아서 출력한다.
print(f'Batch Loss1:  {l1.item():.4f} \nBatch Loss2: {l2.data:.4f}')