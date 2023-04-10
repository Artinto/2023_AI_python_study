from torch import nn, optim, from_numpy
import numpy as np

xy = np.loadtxt('./data/diabetes.csv.gz', delimiter=',', dtype=np.float32)
# csv파일로부터 데이터 로드, ','기준으로 분리, 23비트 실수=>x,y로 나눌것
x_data = from_numpy(xy[:, 0:-1]) #마지막 열 제외한 데이터 기입
y_data = from_numpy(xy[:, [-1]]) #마지막 열의 데이터만 기입
print(f'X\'s shape: {x_data.shape} | Y\'s shape: {y_data.shape}')
#각 데이터의 shape 출력

class Model(nn.Module):
  # class 선언
    def __init__(self):
        # 초기화 메서드
        super(Model, self).__init__()
        self.l1 = nn.Linear(8, 6)
        self.l2 = nn.Linear(6, 4)
        self.l3 = nn.Linear(4, 1)
#a,b =>a개의 입력, b개의 출력 인 선형함수
        self.sigmoid = nn.Sigmoid()
# sigmoid 함수 선언
    def forward(self, x):
        out1 = self.sigmoid(self.l1(x)) #l1까지의 sigmoid 값 저장
        out2 = self.sigmoid(self.l2(out1)) #l2까지의 sigmoid 값 저장
        y_pred = self.sigmoid(self.l3(out2)) #이후의 sigmoid 값 저장
        return y_pred


# our model
model = Model()

criterion = nn.BCELoss(reduction='mean') #이진 분류기에 오차값을 BCE(Binary Cross Entropy)loss로 구함
optimizer = optim.SGD(model.parameters(), lr=0.1) #learning rate :0.1

# Training loop
for epoch in range(100):
    y_pred = model(x_data) #model=Model을 통해 메서드 가져옴 

    loss = criterion(y_pred, y_data)
    print(f'Epoch: {epoch + 1}/100 | Loss: {loss.item():.4f}')
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    #최적화
