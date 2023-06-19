from torch.utils.data import TensorDataset, DataLoader
import torch
from knock72 import X_train, y_train

class LogisticRegression(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(300, 4),
        )
    def forward(self, X):
        return self.net(X)

model = LogisticRegression()
ds = TensorDataset(X_train, y_train)
# DataLoaderを作成
loader = DataLoader(ds, batch_size=1, shuffle=True)

loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.net.parameters(), lr=1e-1)

for epoch in range(10):
    for xx, yy in loader:
        y_pred = model(xx)
        loss = loss_fn(y_pred, yy)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()