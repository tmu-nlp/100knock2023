'''
84. 単語ベクトルの導入Permalink
事前学習済みの単語ベクトル（例えば，Google Newsデータセット（約1,000億単語）
での学習済み単語ベクトル）で単語埋め込みemb(x)を初期化し，学習せよ．
'''

# Colab
# https://colab.research.google.com/drive/1CDF6ds6FzLyrZvsEMQ05PYMHRIY5Evgz?usp=sharing

import torch
from torch import nn
from torch import cuda

import numpy as np
import pandas as pd
import gdown
from gensim.models import KeyedVectors

from knock80 import make_word2id_dictionary, make_train_valid_test, tokenizer
from knock81 import RNN, CreateDataset
from knock82 import train_model, visualize_logs, calculate_loss_and_accuracy


url = 'https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM'
output = 'GoogleNews-vectors-negative300.bin.gz'
gdown.download(url, output, quiet=False)

##################
# データの読み込みとword2id辞書の作成
##################

# csvの読み込み
df = pd.read_csv('./newsCorpora.csv', header=None, sep='\t', quoting=3, names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

# データの抽出
df = df.loc[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), ['TITLE', 'CATEGORY']]

# train, test, validの分割
train, valid, test = make_train_valid_test(df)

# ラベルベクトルの作成
category_dict = {'b': 0, 't': 1, 'e':2, 'm':3}
y_train = train['CATEGORY'].map(lambda x: category_dict[x]).values
y_valid = valid['CATEGORY'].map(lambda x: category_dict[x]).values
y_test = test['CATEGORY'].map(lambda x: category_dict[x]).values

word2id = make_word2id_dictionary(train['TITLE'])

# 学習済みモデルのロード
model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)

# 学習済み単語ベクトルの取得
VOCAB_SIZE = len(word2id) + 1  # 辞書のID数 + パディングID
EMB_SIZE = 300
weights = np.zeros((VOCAB_SIZE, EMB_SIZE))

for i, word in enumerate(word2id.keys()):
  try:
    weights[i] = model[word] # GoogleNews-vectors-negative300
  except KeyError:
    weights[i] = np.random.normal(scale=0.4, size=(EMB_SIZE,))
weights = torch.from_numpy(weights.astype((np.float32)))

################
# RNNによる学習
################

# パラメータの設定
VOCAB_SIZE = len(word2id) + 1  # 辞書のID数 + パディングID
EMB_SIZE = 300
PADDING_IDX = len(word2id)
OUTPUT_SIZE = 4
HIDDEN_SIZE = 50
LEARNING_RATE = 1e-3
BATCH_SIZE = 1
NUM_EPOCHS = 10

# Datasetの作成
dataset_train = CreateDataset(train['TITLE'], y_train, tokenizer)
dataset_valid = CreateDataset(valid['TITLE'], y_valid, tokenizer)
dataset_test = CreateDataset(test['TITLE'], y_test, tokenizer)

# モデルの定義
model = RNN(VOCAB_SIZE, EMB_SIZE, PADDING_IDX, OUTPUT_SIZE, HIDDEN_SIZE)

# 損失関数の定義
criterion = nn.CrossEntropyLoss()

# オプティマイザの定義
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE)


# デバイスの指定
device = 'cuda' if cuda.is_available() else 'cpu'

# モデルの学習
log = train_model(dataset_train, dataset_valid, BATCH_SIZE, model, criterion, optimizer, NUM_EPOCHS)

# ログの可視化
visualize_logs(log)

# 正解率の算出
_, acc_train = calculate_loss_and_accuracy(model, dataset_train, device)
_, acc_test = calculate_loss_and_accuracy(model, dataset_test, device)
print(f'正解率（学習データ）：{acc_train:.3f}')
print(f'正解率（評価データ）：{acc_test:.3f}')
