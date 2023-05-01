import torch # torch import
import torch.nn as nn # 뒤에서 RNN을 사용하기 위해서 import
from torch.autograd import Variable # backpropagation과정에서 사용자의 편의를 위해서 자동 미분이 가능한 Variable을 사용.
# 현재는 모든 tensor에 대해 autograd가 가능하여 사용하지 않아도 괜찮다.

# One hot encoding for each char in 'hello'
# 입력으로 들어가는 Hello에 대한 각 one-hot encoding. l은 두번 사용되므로 한번만 사용해준다.
h = [1, 0, 0, 0] 
e = [0, 1, 0, 0]
l = [0, 0, 1, 0]
o = [0, 0, 0, 1]

# One cell RNN input_dim (4) -> output_dim (2). sequence: 
cell = nn.RNN(input_size=4, hidden_size=2, batch_first=True) # 입력을 4차원, hidden state를 2차원으로 설정 
# batch_fist를 통해서 입력을 [Sequence길이, batchsize, hiddensize]-> [batchsize, sequence길이, hidden size]로 설정
# (num_layers * num_directions, batch, hidden_size) whether batch_first=True or False
hidden = Variable(torch.randn(1, 1, 2)) # hidden state 정의 shape(1,1,2), 값은 평균이 0이고 표준편차가 1인 정규분포 난수 -> 위에서 2로 설정했으므로
# hidden sate는 위의 batch_first랑 상관없이 (num_layers * num_directions, batch, hidden_size)가 된다.
# num_lyaers = RNN 모델의 층 수, num_directions = RNN 모델의 방향 수(위에서는 단방향(!)), batch size는 배치크기, hidden state는 hidden state의 크기를 의미.

# Propagate input through RNN
# Input: (batch, seq_len, input_size) when batch_first=True
inputs = Variable(torch.Tensor([h, e, l, l, o])) # 앞서서 원한 encoding한 것을 hello의 형태로 넣어줌.
for one in inputs:
    one = one.view(1, 1, -1) # 기본 1D Tensor(4)를 3D(1,1,4)로 바꿈 RNN은 3차원 데이터를 입력으로 받으므로.. 
    # Input: (batch, seq_len, input_size) when batch_first=True
    out, hidden = cell(one, hidden) # hello 각 하나의 문자와 이전의 hidden sate를 RNN 모델에 넣어서 결과와 현재의hidden 값을 가진다. 
    print("one input size", one.size(), "out size", out.size(), 'hidden size', hidden.size()) # 입력 크기와 출력 크기 확인/
    # 출력의 크기는 (batch_size, seq_len, hidden_size)가 된다.
# We can do the whole at once
# Propagate input through RNN
# Input: (batch, seq_len, input_size) when batch_first=True
inputs = inputs.view(1, 5, -1) # 입력이 기존에는 one-hot encoding이 hello의 총 5개로 (5,4) -> (1, 5, 4)로 바꿈.
out, hidden = cell(inputs, hidden) # 기존의 sequence 길이는 문자하나만 사용해서 1이 였지만, 여기는 Hello 전부이므로 5이다. 
print("sequence input size", inputs.size(), "out size", out.size(), 'hidden size', hidden.size())


# hidden : (num_layers * num_directions, batch, hidden_size) whether batch_first=True or False
hidden = Variable(torch.randn(1, 3, 2)) # hidden size 변경 뒤에서 입력의 batch_size = 3이므로.

# One cell RNN input_dim (4) -> output_dim (2). sequence: 5, batch 3
# 3 batches 'hello', 'eolll', 'lleel'
# rank = (3, 5, 4)
inputs = Variable(torch.Tensor([[h, e, l, l, o],
                                [e, o, l, l, l],
                                [l, l, e, e, l]]))
# Propagate input through RNN
# Input: (batch, seq_len, input_size) when batch_first=True
# B x S x I
out, hidden = cell(inputs, hidden)
print("batch input size", inputs.size(), "out size", out.size(), 'hidden size', hidden.size())


# One cell RNN input_dim (4) -> output_dim (2)
cell = nn.RNN(input_size=4, hidden_size=2) # batch_first = True를 빼버림. 순서가 [seq_len, batch_size, input_size]

# The given dimensions dim0 and dim1 are swapped.
inputs = inputs.transpose(dim0=0, dim1=1) # batch_first가 없어서 순서를 기존에 정의된 순서를 바꿔줌.
# Propagate input through RNN
# Input: (seq_len, batch_size, input_size) when batch_first=False (default)
# S x B x I
out, hidden = cell(inputs, hidden) # 입력이 변경되어서 들어감.
print("batch input size", inputs.size(), "out size", out.size(), 'hidden size', hidden.size()) # output도 마찬가지로 바뀜.