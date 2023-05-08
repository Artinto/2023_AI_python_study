import time
import math
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import DataLoader
from name_dataset import NameDataset  
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Parameters and DataLoaders
HIDDEN_SIZE = 100
N_CHARS = 128  # ASCII 아스키 코드 = 128개
N_CLASSES = 18 # 나라의 총 개수

class RNNClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers=1): 
      # 클래스 인스턴스 변수로 hidden_size와 n_layers를 저장
        super(RNNClassifier, self).__init__()
        self.hidden_size = hidden_size # 입력된 hidden_size를 받음
        self.n_layers = n_layers # 사용한 n_layers는 기본값 1

        self.embedding = nn.Embedding(input_size, hidden_size)
        # input_size와 hidden_size의 크기로 nn.Embedding 레이어를 정의
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers) 
        # 이어서 nn.GRU 레이어를 정의
        self.fc = nn.Linear(hidden_size, output_size)
        # fully connected 레이어(nn.Linear)를 사용하여 output_size의 클래스 개수를 예측

    def forward(self, input):
        # Note: we run this all at once (over the whole input sequence)
        # input = B x S . size(0) = B
        batch_size = input.size(0) # 배치의 크기를 계산

        input = input.t() # transpose # batch_first가 없으므로 순서를 변경
        print("  input", input.size())
        embedded = self.embedding(input)
        print("  embedding", embedded.size())

        # Make a hidden
        hidden = self._init_hidden(batch_size)
        print('  hidden1 :', hidden.size())
        output, hidden = self.gru(embedded, hidden)
        print("  gru hidden output", hidden.size())
        # _init_hidden 메소드를 사용하여 batch_size x hidden_size 크기의 초기 은닉 상태 생
        print("  gru output", output.size())
        # Use the last layer output as FC's input
        # No need to unpack, since we are going to use hidden
        fc_output = self.fc(hidden)
        print("  fc output", fc_output.size())
        # GRU의 출력값 output은 입력 시퀀스의 모든 시점에 대한 은닉 상태를 갖고 있으며, hidden은 마지막 시점의 은닉 상태만을 갖고 있음
        return fc_output

    def _init_hidden(self, batch_size):
        hidden = torch.zeros(self.n_layers, batch_size, self.hidden_size)
      # batch_size와 hidden_size를 이용하여 크기가 n_layers x batch_size x hidden_size인 0으로 채워진 텐서를 생성
        return Variable(hidden)
# Variable 객체로 변환하여 반환

# Help functions
def str2ascii_arr(msg):
    arr = [ord(c) for c in msg]
    return arr, len(arr)
# 문자열 msg를 입력으로 받아, 해당 문자열의 각 문자를 아스키코드로 변환한 리스트 arr과 문자열의 길이 len(arr)을 반환
# pad sequences and sort the tensor
def pad_sequences(vectorized_seqs, seq_lengths):
    seq_tensor = torch.zeros((len(vectorized_seqs), seq_lengths.max())).long() 
  # 리스트의 길이와 가장 긴 시퀀스의 길이를 곱한 크기의 제로텐서 생
    for idx, (seq, seq_len) in enumerate(zip(vectorized_seqs, seq_lengths)): 
        seq_tensor[idx, :seq_len] = torch.LongTensor(seq) 
    # 각 시퀀스의 인덱스를 참조하여 시퀀스의 길이만큼 해당 텐서의 값을 갱신
    return seq_tensor
def make_variables(names):
    sequence_and_length = [str2ascii_arr(name) for name in names]
    vectorized_seqs = [sl[0] for sl in sequence_and_length]
    seq_lengths = torch.LongTensor([sl[1] for sl in sequence_and_length]) 
    return pad_sequences(vectorized_seqs, seq_lengths) 


if __name__ == '__main__': 
    names = ['adylov', 'solan', 'hard', 'san'] 
    classifier = RNNClassifier(N_CHARS, HIDDEN_SIZE, N_CLASSES) 
 # 이름 리스트 names를 입력으로 받아, str2ascii_arr 함수를 이용하여 각 이름을 아스키코드로 변환
    for name in names: 
        arr, _ = str2ascii_arr(name) 
        inp = Variable(torch.LongTensor([arr]))
        out = classifier(inp) 
        print("in", inp.size(), "out", out.size()) 


    inputs = make_variables(names) 
    out = classifier(inputs)
    print("batch in", inputs.size(), "batch out", out.size()) 
