import torch
import torch.nn as nn
from torch.autograd import Variable

#  "hello" 문자열을 one-hot encoding 형태로 정의
#  input_dim이 4이고 output_dim이 2인 RNN 모델 생성
h = [1, 0, 0, 0]
e = [0, 1, 0, 0]
l = [0, 0, 1, 0]
o = [0, 0, 0, 1]

# batch_first가 True로 설정되어 있어서 입력 데이터의 shape가 (batch_size, sequence_length, input_size)로 지정
cell = nn.RNN(input_size=4, hidden_size=2, batch_first=True)

#  PyTorch의 torch 모듈을 사용하여 랜덤한 값을 가지는 (1, 1, 2) 크기의 텐서를 생성한 후, Variable() 함수를 사용하여 이를 변수에 할당
hidden = Variable(torch.randn(1, 1, 2))

# 인코딩할 문자열 'hello'를 one-hot encoding하여 입력 데이터로 사용
inputs = Variable(torch.Tensor([h, e, l, l, o]))

for one in inputs:
    out, hidden = cell(one, hidden)
#  문자열을 한 글자씩 RNN 셀에 입력하고, 각 입력마다 출력과 새로운 hidden state를 반환
# 이 때, batch_first=True이기 때문에 입력 데이터의 크기는 (1, 1, 4)
inputs = inputs.view(1, 5, -1)
# 입력 데이터를 (batch_size, sequence_length, input_size) 크기로 변경. 이 때, batch_size=1, input_size=4
out, hidden = cell(inputs, hidden)
# 든 문자를 한번에 RNN 셀에 입력하고, 각 입력마다 출력과 새로운 hidden state를 반환
print("sequence input size", inputs.size(), "out size", out.size())

hidden = Variable(torch.randn(1, 3, 2))
# batch_size=3인 입력 데이터를 위한 초기 hidden state을 정의
inputs = Variable(torch.Tensor([[h, e, l, l, o],
                                [e, o, l, l, l],
                                [l, l, e, e, l]]))

# batch_size=3인 입력 데이터를 one-hot encoding하여 정의
out, hidden = cell(inputs, hidden)
# batch_size=3인 입력 데이터를 RNN 셀에 입력하고, 각 입력마다 출력과 새로운 hidden state를 반환
print("batch input size", inputs.size(), "out size", out.size())

cell = nn.RNN(input_size=4, hidden_size=2)
# argument를 default인 False로 설정한 새로운 RNN 셀을 정의

inputs = inputs.transpose(dim0=0, dim1=1)
#  입력 데이터의 차원을 바꿔주어 batch_first=False로 RNN 셀을 적용할 수 있게 
out, hidden = cell(inputs, hidden)
# batch_size=3인 입력 데이터를 batch_first=False로 RNN 셀에 입력하고, 각 입력마다 출력과 새로운 hidden state를 반환
print("batch input size", inputs.size(), "out size", out.size())
