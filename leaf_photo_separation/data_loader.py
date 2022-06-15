
import torch

DEVICE = torch.device('cpu')

BATCH_SIZE = 256
EPOCH = 30

import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

transform_base = transforms.Compose([transforms.Resize((64,64)),
                                     transforms.ToTensor()])
train_dataset = ImageFolder(root='./splitted/train',
                            transform=transform_base)
val_dataset = ImageFolder(root='./splitted/val',
                          transform=transform_base)

from torch.utils.data import DataLoader

train_loader = torch.utils.data.DataLoader(train_dataset,
                                           batch_size=BATCH_SIZE, shuffle=True,
                                           num_workers=4)
val_loader = torch.utils.data.DataLoader(val_dataset,
                                         batch_size=BATCH_SIZE, shuffle=True, num_workers=4)
