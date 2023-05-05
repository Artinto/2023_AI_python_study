import time
import math
import torch
import torch.nn as nn # Neuron Network들을 사용하기 위해서 설치
from torch.autograd import Variable # autograd 기능을 제공하던 변수
from torch.utils.data import DataLoader # 데이터 관리의 편리성을 위해서 설치

from name_dataset import NameDataset  # 다른 파일에서 선언한 모듈 불러오기
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence 
# RNN 학습이 다양한 길이를 연산하여 학습시키기 위해 padding하여 넣어준다

# Parameters and DataLoaders
HIDDEN_SIZE = 100 # 학습할 사이즈 지정
N_CHARS = 128  # ASCII 아스키 코드가 0 ~ 127
N_CLASSES = 18 # 사용되는 나라 개수

class RNNClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers=1):
        super(RNNClassifier, self).__init__()
        self.hidden_size = hidden_size # hidden_size를 불러옴
        self.n_layers = n_layers # n_layers를 불러옴

        self.embedding = nn.Embedding(input_size, hidden_size) # 임배딩에 입력사이즈와 hidden_layer사이즈를 넣는다
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers) # GRU모델에 각 사이즈와 레이어들을 넣는다
        self.fc = nn.Linear(hidden_size, output_size) # linear함수에 hidden_size를 output_size에 맞춰 연산

    def forward(self, input):
        batch_size = input.size(0)

        input = input.t()

        # Embedding S x B -> S x B x I (embedding size) # Gru 모델에 넣기 위해서 [Sequence길이, batchsize, hiddensize]로 변경
        print("  input", input.size())
        embedded = self.embedding(input) # self.embedding을 거치면 (시퀀스 길이, 배치 크기, 임베딩 차원)의 크기를 갖는 3D 텐서 embedded를 반환
        print("  embedding", embedded.size())

        # Make a hidden
        hidden = self._init_hidden(batch_size) # 배치사이즈를 hidden에 넣어 불러옴
        print('  hidden1 :', hidden.size())
        output, hidden = self.gru(embedded, hidden) # gru모델에 embedded와 hidden에 넣어 연산 후 output, hidden에 저장
        print("  gru hidden output", hidden.size())
        print("  gru output", output.size())
        # Use the last layer output as FC's input
        # No need to unpack, since we are going to use hidden
        fc_output = self.fc(hidden) # 마지막에 output 대신 hidden을 사용.
        print("  fc output", fc_output.size())
        return fc_output

    def _init_hidden(self, batch_size):
        hidden = torch.zeros(self.n_layers, batch_size, self.hidden_size) # 초기에 hidden을 0으로 된 (layer, batch_size, hidden_size)로 결정
        return Variable(hidden)


# Help functions
def str2ascii_arr(msg): # string 된 언어를 아스키표를 이용해서 숫자로 변환 및 글자 수 반환
    arr = [ord(c) for c in msg]
    return arr, len(arr)
# pad sequences and sort the tensor
def pad_sequences(vectorized_seqs, seq_lengths):
    seq_tensor = torch.zeros((len(vectorized_seqs), seq_lengths.max())).long() # 가장 긴 단어의 크기를 기준으로 0차원 tensor형성
    for idx, (seq, seq_len) in enumerate(zip(vectorized_seqs, seq_lengths)): # Zip으로 [97, 100, 121, 108, 111, 118] 묶음
        seq_tensor[idx, :seq_len] = torch.LongTensor(seq) # 위에서 묶어진 데이터를 가지고 와서 Tensor에 값을 넣음
    return seq_tensor
def make_variables(names):
    sequence_and_length = [str2ascii_arr(name) for name in names] # name을 아스키코드로 변환하여 리스트생성
    vectorized_seqs = [sl[0] for sl in sequence_and_length] # 앞서 선언한 리스트를 하나씩 받아 아스키 코드 값만 가지고 와서 리스트로 변환 후 Tensor 생성
    seq_lengths = torch.LongTensor([sl[1] for sl in sequence_and_length]) # 처음에 튜플 선언한 리스트에서 길이만 가지고 와서 리스트로 변환 후 Tensor 생성
    return pad_sequences(vectorized_seqs, seq_lengths) # pad_sequences에 넣어 padding하여 생성


if __name__ == '__main__': # 파일을 직접 실행했을 때만 실행
    names = ['adylov', 'solan', 'hard', 'san'] # 예시 입력
    classifier = RNNClassifier(N_CHARS, HIDDEN_SIZE, N_CLASSES) # 모델 선언

    for name in names:
        arr, _ = str2ascii_arr(name)
        inp = Variable(torch.LongTensor([arr]))
        out = classifier(inp)
        print("in", inp.size(), "out", out.size())


    inputs = make_variables(names)
    out = classifier(inputs)
    print("batch in", inputs.size(), "batch out", out.size())
