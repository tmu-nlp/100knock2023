'''
81. RNNによる予測Permalink
再帰型ニューラルネットワーク（RNN: Recurrent Neural Network）を用い，
単語列xからカテゴリyを予測するモデルとして，次式を実装せよ．
'''
import pandas as pd
import torch
from torch import nn
from torch.utils.data import Dataset
from knock80 import make_train_valid_test, make_word2id_dictionary, tokenizer

# Colab
# https://colab.research.google.com/drive/1CDF6ds6FzLyrZvsEMQ05PYMHRIY5Evgz?usp=sharing

class RNN(nn.Module): # nn.Moduleを継承
  def __init__(self, vocab_size, emb_size, padding_idx, output_size, hidden_size):
    super().__init__()
    self.hidden_size = hidden_size
    self.emb = nn.Embedding(vocab_size, emb_size, padding_idx=padding_idx) # padding_idxは各データの単語数を揃えるために空きを埋めるindex
    self.rnn = nn.RNN(emb_size, hidden_size, nonlinearity='tanh', batch_first=True) # batch_firstをTrueにすると，(seq_len, batch, input_size)と指定されている入力テンソルの型を(batch, seq_len, input_size)にできる
    self.fc = nn.Linear(hidden_size, output_size)

  def forward(self, x):
    self.batch_size = x.size()[0]
    hidden = self.init_hidden(x.device)  # h0のゼロベクトルを作成
    emb = self.emb(x) # 入力単語id列xの埋め込み
    # emb.size() : (batch_size, seq_len, emb_size)
    out, hidden = self.rnn(emb, hidden) # 予測ラベルyと次の隠れ状態
    # out.size() : (batch_size, seq_len, hidden_size)
    out = self.fc(out[:, -1, :])
    # out.size() : (batch_size, output_size)
    return out

  def init_hidden(self, device):
    hidden = torch.zeros(1, self.batch_size, self.hidden_size, device=device)
    return hidden


class CreateDataset(Dataset):
  def __init__(self, X, y, tokenizer):
    self.X = X
    self.y = y
    self.tokenizer = tokenizer

  def __len__(self):  # len(Dataset)で返す値を指定
    return len(self.y)

  def __getitem__(self, index):  # Dataset[index]で返す値を指定
    text = self.X[index]
    inputs = self.tokenizer(text, word2id)

    return {
      'inputs': torch.tensor(inputs, dtype=torch.int64),
      'labels': torch.tensor(self.y[index], dtype=torch.int64)
    }


# csvの読み込み
df = pd.read_csv('./newsCorpora.csv', header=None, sep='\t', quoting=3, names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

# データの抽出
df = df.loc[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), ['TITLE', 'CATEGORY']]

# データの分割
train, valid, test = make_train_valid_test(df)

# ラベルベクトルの作成
category_dict = {'b': 0, 't': 1, 'e':2, 'm':3}
y_train = train['CATEGORY'].map(lambda x: category_dict[x]).values
y_valid = valid['CATEGORY'].map(lambda x: category_dict[x]).values
y_test = test['CATEGORY'].map(lambda x: category_dict[x]).values

# word2id辞書の作成
word2id = make_word2id_dictionary(train['TITLE'])

# パラメータの設定
VOCAB_SIZE = len(word2id) + 1  # 辞書のID数 + パディングID
EMB_SIZE = 300
PADDING_IDX = len(word2id)
OUTPUT_SIZE = 4
HIDDEN_SIZE = 50

# Datasetの作成
dataset_train = CreateDataset(train['TITLE'], y_train, tokenizer)
dataset_valid = CreateDataset(valid['TITLE'], y_valid, tokenizer)
dataset_test = CreateDataset(test['TITLE'], y_test, tokenizer)

# モデルの定義
RNN_model = RNN(VOCAB_SIZE, EMB_SIZE, PADDING_IDX, OUTPUT_SIZE, HIDDEN_SIZE)

# 先頭3件の予測値取得
for i in range(3):
    X = dataset_train[i]['inputs']
    print(torch.softmax(RNN_model(X.unsqueeze(0)), dim=-1))
