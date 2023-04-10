from torch.utils.data import Dataset, DataLoader
# 파이썬의 dataset과 dataloader module을 사용
from torch import from_numpy, tensor
import numpy as np

class DiabetesDataset(Dataset):
# dataset을 상속받아 DiabetesDataset의 클래스 정의
    def __init__(self):
        xy = np.loadtxt('./data/diabetes.csv.gz',
                        delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]
# 받아온 dataset의 전체 샘플 수를 나타냄 (dateset의 총 길이 반환)
        self.x_data = from_numpy(xy[:, 0:-1])
        self.y_data = from_numpy(xy[:, [-1]])

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
# 주어진 index에 해댕하는 데이터 반환 -> 여기서 index는 미니배치 데이터의 index 의미
    def __len__(self):
        return self.len
# dataset의 길이를 반환 -> 미니배치 데이터의 개수를 계산할 때 사용


dataset = DiabetesDataset()
# DiabetesDataset 클래스의 인스턴스를 생성
train_loader = DataLoader(dataset=dataset,
                          batch_size=32,
                          shuffle=True,
                          num_workers=2)
# Pytorch의 dataloader 클래스를 사용하여 데이터셋을 미니배치로 분할하는 과정
# batch_size : 미니배치의 크기를 지정
# shuffle : 데이터셋을 미니배치로 분할하기 전에 데이터셋을 임의로 섞을 것인지를 지정
# num_workers : 데이터로더가 데이터를 불러오는 데 사용할 프로세스(worker)의 수를 지정

for epoch in range(2):
# 2번 반복 학습
    for i, data in enumerate(train_loader, 0):
# enumerate함수 : 데이터로더(train_loader)로부터 미니배치 데이터를 가져옴 -> 미니배치의 인덱스(i)와 미니배치 데이터(data)를 반환 ( 0은 enumerate()함수에서 시작하는 인덱스를 지정)

        inputs, labels = data
# 미니배치 데이터에서 inputs(입력)과 labels(출력)을 가져옴

        inputs, labels = tensor(inputs), tensor(labels)
# NumPy 배열을 PyTorch의 tensor 객체로 변환

        print(f'Epoch: {i} | Inputs {inputs.data} | Labels {labels.data}')
# 미니배치의 인덱스, 입력(inputs) 및 출력(labels) 값을 출력
