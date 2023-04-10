# References
# https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py
# http://pytorch.org/tutorials/beginner/data_loading_tutorial.html#dataset-class
from torch.utils.data import Dataset, DataLoader
from torch import from_numpy, tensor
import numpy as np

class DiabetesDataset(Dataset):
    """ Diabetes dataset."""

    # Initialize your data, download, etc.
    def __init__(self):
        xy = np.loadtxt('/content/drive/MyDrive/Colab Notebooks/test/diabetes.csv',
                        delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]
        # 받아온 dataset 전체 샘플 의 shape을 나타냄
        self.x_data = from_numpy(xy[:, 0:-1])
        self.y_data = from_numpy(xy[:, [-1]])

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
# 주어진 index에 해당하는 데이터를 가져와 반환
    def __len__(self):
        return self.len
        # dataset의 길이를 반환

# dataloader 클래스 작성 : 데이터들을 각각의 데이터셋으로 분리
dataset = DiabetesDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=32,
                          shuffle=True,
                          num_workers=2)
# batch_size : 크기 지정
# shuffle : 랜덤성 부여
# num_workers : 프로세서 수 지정

for epoch in range(2):
    for i, data in enumerate(train_loader, 0):
        # get the inputs
        inputs, labels = data

        # wrap them in Variable
        inputs, labels = tensor(inputs), tensor(labels)

        # Run your training process
        print(f'Epoch: {i} | Inputs {inputs.data} | Labels {labels.data}')
