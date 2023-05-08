import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, transforms

batch_size = 64

device = torch.device('cuda')

transformer = transforms.Compose(
    [transforms.Resize((32, 32)),
     transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

training_dataset = datasets.CIFAR10(root='./data',
                                    train=True,
                                    download=True,
                                    transform=transforms.ToTensor())#이미지를 FLoatTensor 형태로 변환
testing_dataset = datasets.CIFAR10(root='./data',
                                   train=False,
                                   download=True,
                                   transform=transformer)

training_loader = torch.utils.data.DataLoader(dataset=training_dataset,
                                              batch_size=100,
                                              shuffle=True)
testing_loader = torch.utils.data.DataLoader(dataset=testing_dataset,
                                             batch_size=100,
                                             shuffle=False)

classes = ('airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x)))
        x = F.relu(self.mp(self.conv2(x)))
        x = x.view(in_size, -1)  # flatten the tensor
        x = self.fc(x)
        return F.log_softmax(x)

model = Net()

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)
criterion = nn.CrossEntropyLoss()

def train (epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(training_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(training_loader.dataset),
                       100. * batch_idx / len(training_loader), loss.item()))

def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in testing_loader:
        output = model(data)
        # sum up batch loss
        test_loss += F.nll_loss(output, target, size_average=False).data
        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()
