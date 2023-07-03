import torch
from torch import nn
from torch.utils.data import Dataset

class RNN(nn.Module):
  def __init__(self, vocab_size, emb_size, padding_idx, output_size, hidden_size):
    super().__init__()
    self.hidden_size = hidden_size
    self.emb = nn.Embedding(vocab_size, emb_size, padding_idx=padding_idx)
    self.rnn = nn.RNN(emb_size, hidden_size, nonlinearity="tanh", batch_first=True)
    self.fc = nn.Linear(hidden_size, output_size)
    
 def forward(self, x):
    self.batch_size = x.size()[0]
    hidden = self.init_hidden(x.device)
    emb = self.emb(x)
    out, hidden = self.rnn(emb, hidden)
    out = self.fc(out[:, -1, :])
    return out
    
  def init_hidden(self, device):
    hidden = torch.zeros(1, self.batch_size, self.hidden_size, device=device)
    return hidden

class CreateDataset(Dataset):
  def __init__(self, X, y, tokenizer):
    self.X = X
    self.y = y
    self.tokenizer = tokenizer

  def __len__(self)
    return len(self.y)

  def __getitem__(self, index):
    text = self.X[index]
    inputs = self.tokenizer(text)

    return {
      "inputs": torch.tensor(inputs, dtype=torch.int64),
      "labels": torch.tensor(self.y[index], dtype=torch.int64)
    }


# ラベルベクトルの作成
category_dict = {"b": 0, "t": 1, "e":2, "m":3}
y_train = train["CATEGORY"].map(lambda x: category_dict[x]).values
y_valid = valid["CATEGORY"].map(lambda x: category_dict[x]).values
y_test = test["CATEGORY"].map(lambda x: category_dict[x]).values

# Datasetの作成
dataset_train = CreateDataset(train["TITLE"], y_train, tokenizer)
dataset_valid = CreateDataset(valid["TITLE"], y_valid, tokenizer)
dataset_test = CreateDataset(test["TITLE"], y_test, tokenizer)

print(f"len(Dataset)の出力: {len(dataset_train)}")
print("Dataset[index]の出力:")
for var in dataset_train[1]:
  print(f"  {var}: {dataset_train[1][var]}")

# パラメータの設定
VOCAB_SIZE = len(set(word2id.values())) + 1  # 辞書のID数 + パディングID
EMB_SIZE = 300
PADDING_IDX = len(set(word2id.values()))
OUTPUT_SIZE = 4
HIDDEN_SIZE = 50

# モデルの定義
model = RNN(VOCAB_SIZE, EMB_SIZE, PADDING_IDX, OUTPUT_SIZE, HIDDEN_SIZE)

# 先頭10件の予測値取得
for i in range(10):
  X = dataset_train[i]["inputs"]
  print(torch.softmax(model(X.unsqueeze(0)), dim=-1))