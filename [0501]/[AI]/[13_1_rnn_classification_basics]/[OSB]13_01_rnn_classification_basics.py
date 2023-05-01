import time # 보통 학습시간을 확인하기 위해 사용 본 코드에서는 사용되지 않음.
import math # 수학적 연산을 위해서 사용. 본 코드에서는 사용하지않음. 
import torch
import torch.nn as nn # 다양한 Neuron Network들을 사용하기 위해서 사용.
from torch.autograd import Variable # 이전에 pytorch에서 제공하는 autograd 기능을 제공하던 변수. 현재는 모든 Tensor에 대해 autograd를 지원해 사용하지 않아도 무방.
from torch.utils.data import DataLoader # 학습시 batchszie 단위로 학습하며, 데이터 관리의 편리성을 위해서 사용. 본 코드에서는 사용되지 않음.

from name_dataset import NameDataset  # 다른 파일에서 선언한 모듈 불러오기
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
# RNN 학습이 모든 input sequence의 길이가 동일하게 학습되므로 다양한 길이의 sequence를 학습시키기 위해서 padding하여 넣어주고, 실제 계산시 패딩된 부분은 무시하고 계산
# 그리고 pack을 통해서 output을 계산한 뒤에 다시 원래의 길이로 바꿔준다. 본 코드에서는 사용하지 않음.

# Parameters and DataLoaders
HIDDEN_SIZE = 100 # 학습할 수 및 embedding에 사용할 차원
N_CHARS = 128  # ASCII 아스키 코드가 0 ~ 127이므로
N_CLASSES = 18 # 총 사용되는 나라.

class RNNClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers=1):
        super(RNNClassifier, self).__init__()
        self.hidden_size = hidden_size # 사용할 hidden_size는 입력된 것으로 사용
        self.n_layers = n_layers # 사용한 n_layers는 기본값으로 1, 입력으로 바꿔줄 수 있다,

        self.embedding = nn.Embedding(input_size, hidden_size) # 임배딩 입력의 크기와 학습할 hidden_layer의 size를 제공.
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers) # GRU 모델 사용 여기서 hidden_size가 두 개라 이상할 수 있지만, input_size = hidden_size라 상관없음.
        self.fc = nn.Linear(hidden_size, output_size) # 마지막 linear로 18개의 class로 뽑아냄.

    def forward(self, input):
        # Note: we run this all at once (over the whole input sequence)
        # input = B x S . size(0) = B
        batch_size = input.size(0) # 배치의 크기 계산.

        # input:  B x S  -- (transpose) --> S x B # Batch_frist가 없므로 순서 변경.
        input = input.t() # transpose

        # Embedding S x B -> S x B x I (embedding size) # Gru 모델에 넣기 위해서 [Sequence길이, batchsize, hiddensize]로 변경
        print("  input", input.size())
        embedded = self.embedding(input) # 임배딩을 통해 변하는것을 확인.
        print("  embedding", embedded.size())

        # Make a hidden
        hidden = self._init_hidden(batch_size) # 뒤에서 _init_hidden을 이용해서 hidden 선언
        print('  hidden1 :', hidden.size())
        output, hidden = self.gru(embedded, hidden) # gru모델에 입력과, 출력을 넣어줌.
        print("  gru hidden output", hidden.size())
        print("  gru output", output.size())
        # Use the last layer output as FC's input
        # No need to unpack, since we are going to use hidden
        fc_output = self.fc(hidden) # 마지막에 output 대신 hidden을 사용.
        print("  fc output", fc_output.size())
        return fc_output

    def _init_hidden(self, batch_size):
        hidden = torch.zeros(self.n_layers, batch_size, self.hidden_size) # 초기에 hidden을 0으로 된 (layer, batch_size, hidden_size)로 결정 # 원래는 방향성도 고려해야하지만, 여기선 단방향이므로 1
        return Variable(hidden)


# Help functions
def str2ascii_arr(msg): # string 된 언어를 아스키표를 이용해서 숫자로 변환 및 글자 수 반환
    arr = [ord(c) for c in msg]
    return arr, len(arr)
# pad sequences and sort the tensor
def pad_sequences(vectorized_seqs, seq_lengths):
    seq_tensor = torch.zeros((len(vectorized_seqs), seq_lengths.max())).long() # 기존에 가장 긴 단어의 크기를 기반으로 데이터 수 X 최대 단어 길이의 0텐서 생성.
    for idx, (seq, seq_len) in enumerate(zip(vectorized_seqs, seq_lengths)): # Zip을 이용해 각 [97, 100, 121, 108, 111, 118] 과 6 이렇게 튜플로 묶음.
        seq_tensor[idx, :seq_len] = torch.LongTensor(seq) # 위에서 묶어진 데이터를 순차적으로 가지고 와서 0으로 채원진 Tensor에 값을 넣음. -> 자동으로 남은 요소들을 0
    return seq_tensor # 반환
def make_variables(names):
    sequence_and_length = [str2ascii_arr(name) for name in names] # 아스키 코드 반환하여 (아스키 코드 값, 길이) 튜플 형태로 반환 후 리스트로 선언
    vectorized_seqs = [sl[0] for sl in sequence_and_length] # 앞서 선언한 리스트를 하나씩 받아 아스키 코드 값만 가지고 와서 리스트로 변환 후 Tensor 생성.
    seq_lengths = torch.LongTensor([sl[1] for sl in sequence_and_length]) # 처음에 튜플 선언한 리스트에서 길이만 가지고 와서 리스트로 변환 후 Tensor 생성.
    return pad_sequences(vectorized_seqs, seq_lengths) # pad_sequences에 넣어 가장 긴 단어 길이에 맞춰 단어의 길이가 부족하면 0으로 padding하여 생성.


if __name__ == '__main__': # 파일을 직접 실행했을 때만 실행
    names = ['adylov', 'solan', 'hard', 'san'] # 예시 입력
    classifier = RNNClassifier(N_CHARS, HIDDEN_SIZE, N_CLASSES) # 모델 선언

    for name in names: # 예시 입력에 이름이 들어감.
        arr, _ = str2ascii_arr(name) # 출력인 arr은 아스키 코드를 통해 숫자로 반환된 리스트를 가짐.
        inp = Variable(torch.LongTensor([arr])) # 반환된 숫자를 autograd를 사용하기 위해 Variable로 변환 (현재는 그냥 사용해도 무방.)
        out = classifier(inp) # Tensor로 선언한 입력값들을 앞서 선언한 분류모델에 대입.
        print("in", inp.size(), "out", out.size()) # 입력의 크기와 출력의 크기를 확인


    inputs = make_variables(names) # input의 전체 크기 확인
    out = classifier(inputs) # 전체 input에 대한 output 생성
    print("batch in", inputs.size(), "batch out", out.size()) # input, output size 출력

