import numpy
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image

class Model():
    def __init__(self, input_size, output_size):
        self.conv1 = nn.Conv2d(in_channels=4, out_channels=8, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=5)
        self.fc1 = nn.Linear(in_features=16*61*61, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=60, out_features=1)

    def forward(self, img):
        img = t.resize((256, 256)) 
        t = torch.tensor(numpy.array(t)).float()
        if len(t.shape) == 3:
            t = torch.transpose(t, 2, 0)
            t = t.unsqueeze(0)
        else:
            t = torch.transpose(t, 3, 1)
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)
                    
        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)
        
        t = t.reshape(-1, 16 * 61 * 61)
        t = self.fc1(t)
        t = F.relu(t)
        
        t = self.fc2(t)
        t = F.relu(t)
        
        t = self.out(t)
        return F.relu(t)

    def save(self, path):
        torch.save(self.model, path)

    def load(self, path):
        self.model = torch.load(PATH)

if __name__ == "__main__":
    conv1 = nn.Conv2d(in_channels=4, out_channels=8, kernel_size=5)
    conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=5)

    t = Image.open("testing.jpg")
    t = t.resize((256, 256))
    t = torch.tensor(numpy.array(t)).float()
    if len(t.shape) == 3:
        t = torch.transpose(t, 2, 0)
        t = t.unsqueeze(0)
    else:
        t = torch.transpose(t, 3, 1)
    t = conv1(t)
    t = F.relu(t)
    t = F.max_pool2d(t, kernel_size=2, stride=2)
            
    t = conv2(t)
    t = F.relu(t)
    t = F.max_pool2d(t, kernel_size=2, stride=2)

    print("Output size for flatten:", t.shape)
