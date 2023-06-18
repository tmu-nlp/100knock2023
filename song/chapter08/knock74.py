import pandas as pd
import gensim
import numpy as np
import torch
from torch.utils.data import TensorDataset, DataLoader
from knock72 import X_train, y_train
from knock74 import model

def accuracy(pred, label):
  pred = np.argmax(pred.data.numpy(), axis=1)
  label = label.data.numpy()
  return (pred == label).mean()


X_valid = np.loadtxt('X_valid.txt', delimiter=' ')
X_valid = torch.tensor(X_valid, dtype=torch.float32)
y_valid = np.loadtxt('y_valid.txt')
y_valid = torch.tensor(y_valid, dtype=torch.int64)

pred = model(X_train)
print (accuracy(pred, y_train))
pred = model(X_valid)
print (accuracy(pred, y_valid))
