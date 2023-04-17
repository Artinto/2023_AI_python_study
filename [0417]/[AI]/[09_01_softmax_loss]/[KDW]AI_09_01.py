from torch import nn, tensor, max
import numpy as np

# on-hot encoding방식으로 생성
Y = np.array([1, 0, 0])
#Y실제값을 저장 
#예상값 데이터를 정의
Y_pred1 = np.array([0.7, 0.2, 0.1])
#예상값 1
Y_pred2 = np.array([0.1, 0.3, 0.6])
#예상값2(오차 큼)
print(f'Loss1: {np.sum(-Y * np.log(Y_pred1)):.4f}') # 0.35 <- -YlogY(hat)한 값으로 cost를
#구하는 함수로 cross entorpy 기법이다.
print(f'Loss2: {np.sum(-Y * np.log(Y_pred2)):.4f}') # 2.3

#예상값 1과 다르게 2가 cost가 크게 나온 것을 볼 수 있음


#nn.CrossEntropyLoss()는 소프트맥스와 교차 엔트로피 손실 함수를 결합한 PyTorch의 함수입니다.
# Softmax + CrossEntropy (logSoftmax + NLLLoss)
loss = nn.CrossEntropyLoss()
#pytorch함수에서 cross-entorpy를 이용한 loss계산 함수인 loss함수 생성


Y = tensor([0], requires_grad=False)
#위와 다르게 Y를 텐서 형식으로 선언

Y_pred1 = tensor([[2.0, 1.0, 0.1]])
#예상데이터를 텐서 형식으로 선언
Y_pred2 = tensor([[0.5, 2.0, 0.3]])
# 교차 엔트로피 손실 함수를 계산합니다.

l1 = loss(Y_pred1, Y)
#위에서 생성한 loss함수를 통해 예측값과 y데이터를 통해 loss값 계산
#여기서 예측값이 위와 다르게 softmax값이 아니라 logit값을 이용하는데 loss함수에 softmax함수
#가 포함되어 있기 때문
l2 = loss(Y_pred2, Y)

print(f'PyTorch Loss1: {l1.item():.4f} \nPyTorch Loss2: {l2.item():.4f}')
print(f'Y_pred1: {max(Y_pred1.data, 1)[1].item()}') #0.41
print(f'Y_pred2: {max(Y_pred2.data, 1)[1].item()}') # 1.84
# cost 계산

Y = tensor([2, 0, 1], requires_grad=False)
# Y 정답갓을 텐서 형태로 선언

# input is of size nBatch x nClasses = 2 x 4
# Y_pred are logits (not softmax)
Y_pred1 = tensor([[0.1, 0.2, 0.9], # 인덱스 2가 가장 큼 -> GOOD
                  [1.1, 0.1, 0.2], # 인덱스 0이 가장 큼 -> GOOD
                  [0.2, 2.1, 0.1]]) #인덱스 1이 가장 큼 -> GOOD

Y_pred2 = tensor([[0.8, 0.2, 0.3], #BAD
                  [0.2, 0.3, 0.5],#BAD
                  [0.2, 0.2, 0.5]])#BAD

# 교차 엔트로피 손실 함수를 계산합니다.
l1 = loss(Y_pred1, Y)
l2 = loss(Y_pred2, Y)
#위에 예측값을 통해 LOSS값 계산 마찬가지로 softmax형태 아니여도 됨
print(f'Batch Loss1:  {l1.item():.4f} \nBatch Loss2: {l2.data:.4f}')
