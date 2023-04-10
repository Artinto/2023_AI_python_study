from torch.utils.data import Dataset, DataLoader
# \ dataset,dataloader 모듈
from torch import from_numpy, tensor
import numpy as np

class DiabetesDataset(Dataset):
    # dataset을 상속받은 DiabetesDataset 클래스 정의
    def __init__(self):
        xy = np.loadtxt('./data/diabetes.csv.gz',
                        delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]
        self.x_data = from_numpy(xy[:, 0:-1])
        self.y_data = from_numpy(xy[:, [-1]])
        #csv파일을 읽어온 후 xdata와 ydata를 초기화 
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
        #index에 대한 xdata와 ydata를 반환해주는 함수
    def __len__(self):
        return self.len
        #데이터 길이를 반환해주는 함수

dataset = DiabetesDataset()
# DiabetesDataset 객채를 생성
train_loader = DataLoader(dataset=dataset,
                          batch_size=32,
                          shuffle=True,
                          num_workers=2)
# 사용할 데이터로더를 선언, dataset은 사용할 데이터셋을 지정해줌, batch_size는 전체 데이터를 분할할 배치 사이즈를 설정, 
#Epoch마다 데이터셋을 섞어서 데이터가 학습되는 순서를 바꿈 ,num_workers는 작업에 사용할 cpu 코어수를 설정

for epoch in range(2):
    for i, data in enumerate(train_loader, 0):
        # enumerate함수를 통해 데이터로더로부터 배치 정보를 가져옴, 0 인자값은 0인덱스부터 모두 가져오는 것을 의미하고 i와 data를 반환

        inputs, labels = data
        # 배치 데이터인 data변수에서 inputs과 labels을 가져옴 (입력, 출력)

        inputs, labels = tensor(inputs), tensor(labels)
        # numpy배열 데이터를 토치의 tensor형태로 바꿈

        print(f'Epoch: {i} | Inputs {inputs.data} | Labels {labels.data}')
        #배치의 인덱스, 입력 출력값 프린트
