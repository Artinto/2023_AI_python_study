from torch import nn, optim, from_numpy
import numpy as np

xy = np.loadtxt('/content/drive/MyDrive/Colab Notebooks/test/diabetes.csv', delimiter=',', dtype=np.float32)
# diabetes.csv.gz데이터시트를 불러옴
x_data = from_numpy(xy[:, 0:-1])
# 각 행의 마지막 열 빼고 나머지 열을 가져옴
y_data = from_numpy(xy[:, [-1]])
# 각 행의 마지막 열을 가져옴
print(f'X\'s shape: {x_data.shape} | Y\'s shape: {y_data.shape}')


class Model(nn.Module):
    def __init__(self):
        """
        In the constructor we instantiate two nn.Linear module
        """
        super(Model, self).__init__()
        self.l1 = nn.Linear(8, 6) # input 8개를 받아 output을 6개 배출
        self.l2 = nn.Linear(6, 4) # self.11에서 도출된 output 6개를 sigmoid에 넣어 나온 결과 6개를 그대로 input에 넣고 4개의 output을 도출
        self.l3 = nn.Linear(4, 1) # 위와 같은 형식

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        """
        In the forward function we accept a Variable of input data and we must return
        a Variable of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Variables.
        """
        out1 = self.sigmoid(self.l1(x))
        out2 = self.sigmoid(self.l2(out1))
        y_pred = self.sigmoid(self.l3(out2))
        return y_pred # 반복된 클래스를 통해 최종결과물 1차원의 데이터를 반환


# our model
model = Model()


# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the model.
criterion = nn.BCELoss(reduction='mean')
# 로스함수를 BCELoss를 사용하여 이진 분류를 수행, reduction은 손실 계산에 대한 리덕션 방식을 지정하고 'mean'요소별 손실 값을 평균내고, 전체으 편균 손실을 값을 나타내는 스칼라 텐서로 반환
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Training loop
for epoch in range(100):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)

    # Compute and print loss
    loss = criterion(y_pred, y_data)
    print(f'Epoch: {epoch + 1}/100 | Loss: {loss.item():.4f}')

    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
