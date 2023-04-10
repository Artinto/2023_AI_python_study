# References
# https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py
# http://pytorch.org/tutorials/beginner/data_loading_tutorial.html#dataset-class
from torch.utils.data import Dataset, DataLoader
from torch import from_numpy, tensor
import numpy as np

class DiabetesDataset(Dataset):
    def __init__(self):
      #초기화메서드
        xy = np.loadtxt('./data/diabetes.csv.gz',
                        delimiter=',', dtype=np.float32)
        self.len = xy.shape[0] 
        self.x_data = from_numpy(xy[:, 0:-1]) #마지막열 제외
        self.y_data = from_numpy(xy[:, [-1]]) #마지막열만

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


dataset = DiabetesDataset()
train_loader = DataLoader(dataset=dataset #DataLoder 클래스 통해 데이터셋을 미니배치로 분할
                          batch_size=32, #미니배치의 사이즈
                          shuffle=True, #미니배치 분할 전 램덤으로 섞을지 판단
                          num_workers=2) #데이터를 불러오는데 이용될 프로세스 수 지정

for epoch in range(2):
    for i, data in enumerate(train_loader, 0):
        #enumerate 함수 : dataloader에서 미니배치 데이터 가져옴
        inputs, labels = data

        # wrap them in Variable
        inputs, labels = tensor(inputs), tensor(labels)

        # Run your training process
        print(f'Epoch: {i} | Inputs {inputs.data} | Labels {labels.data}')
