
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from data_loader import DEVICE, torch

class Net(nn.Module): # nn.Module을 상속한다. (필수코드)
    def __init__(self):

        super(Net, self).__init__() # 필수코드

        self.conv1 = nn.Conv2d(3, 32, 3, padding=1) # 컨볼루젼 레이어
        self.pool = nn.MaxPool2d(2, 2) # 풀링 레이어
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1) # 컨볼루젼 레이어
        self.conv3 = nn.Conv2d(64, 64, 3, padding=1) # 컨볼루젼 레이어

        self.fc1 = nn.Linear(4096, 512)
        self.fc2 = nn.Linear(512, 33)

    def forward(self, x):

        x = self.conv1(x)
        x = F.relu(x)
        x = self.pool(x)
        x = F.dropout(x, p=0.25, training=self.training)

        x = self.conv2(x)
        x = F.relu(x)
        x = self.pool(x)
        x = F.dropout(x, p=0.25, training=self.training)

        x = self.conv3(x)
        x = F.relu(x)
        x = self.pool(x)
        x = F.dropout(x, p=0.25, training=self.training)

        x = x.view(-1, 4096)
        x = self.fc1(x)
        x = F.relu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        x = self.fc2(x)

        return F.log_softmax(x, dim=1)

model_base = Net().to(DEVICE)
optimizer = optim.Adam(model_base.parameters(), lr=0.001)




