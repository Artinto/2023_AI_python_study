from torch import nn, tensor, max
import numpy as np

Y = np.array([1, 0, 0])
# Y실제값 저장 
Y_pred1 = np.array([0.7, 0.2, 0.1])
# 예상 값을 Y_pred1에 저장
Y_pred2 = np.array([0.1, 0.3, 0.6])
# 예상 값을 Y_pred2에 저장
print(f'Loss1: {np.sum(-Y * np.log(Y_pred1)):.4f}')
#cross entorpy
print(f'Loss2: {np.sum(-Y * np.log(Y_pred2)):.4f}')

loss = nn.CrossEntropyLoss()
# cross-entorpy를 이용해 loss함수 생성


Y = tensor([0], requires_grad=False)
#Y를 텐서 형식으로 선언

#텐서 형식 선언
Y_pred1 = tensor([[2.0, 1.0, 0.1]])
Y_pred2 = tensor([[0.5, 2.0, 0.3]])

l1 = loss(Y_pred1, Y)
l2 = loss(Y_pred2, Y)

print(f'PyTorch Loss1: {l1.item():.4f} \nPyTorch Loss2: {l2.item():.4f}')
print(f'Y_pred1: {max(Y_pred1.data, 1)[1].item()}') #0.41
print(f'Y_pred2: {max(Y_pred2.data, 1)[1].item()}') # 1.84
# cost 계산

Y = tensor([2, 0, 1], requires_grad=False)
# Y의 결과값을 텐서 형태로 선언

# input is of size nBatch x nClasses = 2 x 4
# Y_pred are logits (not softmax)
Y_pred1 = tensor([[0.1, 0.2, 0.9], 
                  [1.1, 0.1, 0.2], 
                  [0.2, 2.1, 0.1]])

Y_pred2 = tensor([[0.8, 0.2, 0.3],
                  [0.2, 0.3, 0.5],
                  [0.2, 0.2, 0.5]])#

# 교차 엔트로피 손실 함수를 계산
l1 = loss(Y_pred1, Y)
l2 = loss(Y_pred2, Y)
print(f'Batch Loss1:  {l1.item():.4f} \nBatch Loss2: {l2.data:.4f}')
