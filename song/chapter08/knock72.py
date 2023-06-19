import torch
import numpy as np
import gensim
from knock71 import X_train

softmax = torch.nn.Softmax(dim=1)
W = torch.randn(300, 4)

y_train = np.loadtxt('./song/chapter08/y_train.txt')
y_train = torch.tensor(y_train, dtype=torch.int64)
loss = torch.nn.CrossEntropyLoss()
print (loss(torch.matmul(X_train[:1], W),y_train[:1]))
print (loss(torch.matmul(X_train[:4], W),y_train[:4]))

ans = [] # 以下、確認
for s,i in zip(softmax(torch.matmul(X_train[:4], W)),y_train[:4]):
  ans.append(-np.log(s[i]))
print (np.mean(ans))