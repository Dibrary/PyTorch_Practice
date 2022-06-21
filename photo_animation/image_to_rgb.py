
import glob
import random
import os
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torchvision.transforms as transforms
import sys
import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
import math
import itertools
import datetime, time
from torchvision.utils import save_image, make_grid
from torchvision import datasets
from torch.autograd import Variable

def to_rgb(image):
    rgb_image = Image.new("RGB", image.size)
    rgb_image.paste(image)
    return rgb_image




