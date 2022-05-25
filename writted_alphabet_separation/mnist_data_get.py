import torch
import torch.optim as optim
from torchvision import datasets, transforms

import matplotlib.pyplot as plt
# %matplotlib inline

device = torch.device('cpu') # CUDA를 안 씀.

batch_size = 50 # 가중치 업데이트 시 필요 샘플 갯수
epoch_num = 15 # 학습 기본 단위 횟수
learning_rate = 0.0001 # 학습률

# train_data = datasets.MNIST(root='./data', train=True, download=True,transform=transforms.ToTensor()) # 코드 진행 후 data폴더 생김
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transforms.ToTensor())
test_data = datasets.MNIST(root='./data', train=False, transform=transforms.ToTensor())

print('number of training data: ', len(train_data))
print('number of testing data: ', len(test_data))

# image, label = train_data[0] 첫 번째 데이터 확인 용 코드

train_loader = torch.utils.data.DataLoader(dataset=train_data,batch_size=batch_size,shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_data,batch_size=batch_size,shuffle=True)

first_batch = train_loader.__iter__().__next__()
print("first_batch", str(type(first_batch)), len(first_batch))
print("first_batch[0]", str(type(first_batch[0])), first_batch[0].shape) # (배치크기, 채널, width, height)
print("first_batch[1]", str(type(first_batch[1])), first_batch[1].shape) # 기설정한 batch_size다.











