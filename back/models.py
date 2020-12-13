import numpy
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image

class Conv2D(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=input_size, out_channels=8, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=5)
        self.fc1 = nn.Linear(in_features=16*61*61, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=60, out_features=output_size)

    def forward(self, img):
        img = img.resize((256, 256)) 
        t = torch.tensor(numpy.array(img)).float()
        t = torch.transpose(t, 2, 0)
        t = t.unsqueeze(0)
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
        return F.sigmoid(t)

class Model():
    def __init__(self, modelClass, lr=0.01):
        self.lr = lr
        self.model = modelClass(4, 5)
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)

    def save(self, path):
        torch.save(self.model, path)
    
    def load(self, path):
        self.model = torch.load(path)
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr)

    def train(self, img, scores):
        self.optimizer.zero_grad()
        pred = self.model(img)
        scores = torch.tensor(scores).unsqueeze(0).float()
        loss = self.criterion(pred, scores)
        loss.backward()
        self.optimizer.step()
        return pred.detach().tolist()

    def predict(self, image):
        with torch.no_grad():
            return self.model(image).detach().tolist()
        


if __name__ == "__main__":
    conv1 = nn.Conv2d(in_channels=4, out_channels=8, kernel_size=5)
    conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=5)

    t = Image.open("model_train.jpg")
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

    model = Model(Conv2D)
    print("Testing prediction:", model.predict(Image.open("model_train.jpg")))
    model.save("conv2d.torch")
