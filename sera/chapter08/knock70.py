import pandas as pd
from sklearn.model_selection import train_test_split
from gensim.models import KeyedVectors
import gdown

df = pd.read_csv("newsCorpora.csv", header=None, sep="\t", names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

df = df.loc[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]), ["CATEGORY", "TITLE"]]
df = df.sample(frac=1, ignore_index=True, random_state=42)

train, valid_test = train_test_split(df, test_size=0.2)
valid, test = train_test_split(valid_test, test_size=0.5)

url = "https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM"
output = "GoogleNews-vectors-negative300.bin.gz"
gdown.download(url, output, quiet=True)
model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)

#特徴量行列とベクトルを作成
import string
import torch

def transform_w2v(text):
  table = str.maketrans(string.punctuation, " "*len(string.punctuation)) # 置換元文字は記号、置換後文字はスペース
  words = text.translate(table).split(" ")  # 記号をスペースに置換後、スペースで分割してリスト化
  vec = [model[word] for word in words if word in model]  # 1語ずつベクトル化

  return torch.tensor(sum(vec) / len(vec))  # 平均ベクトルをTensor型に変換して返す

#特徴ベクトルの作成（得られるベクトルを一つのテンソルにまとめている）
X_train = torch.stack([transform_w2v(text) for text in train["TITLE"]])
X_valid = torch.stack([transform_w2v(text) for text in valid["TITLE"]])
X_test = torch.stack([transform_w2v(text) for text in test["TITLE"]])

#ラベルベクトルの作成
category_dict = {"b": 0, "t": 1, "e":2, "m":3}
y_train = torch.tensor(train["CATEGORY"].map(lambda x: category_dict[x]).values) # trainデータセットのCATEGORY列をcategory_dictを使って数値ラベルに変換し、PyTorchのテンソルに変換したもの
y_valid = torch.tensor(valid["CATEGORY"].map(lambda x: category_dict[x]).values)
y_test = torch.tensor(test["CATEGORY"].map(lambda x: category_dict[x]).values)

#保存
torch.save(X_train, "X_train.pt")
torch.save(X_valid, "X_valid.pt")
torch.save(X_test, "X_test.pt")
torch.save(y_train, "y_train.pt")
torch.save(y_valid, "y_valid.pt")
torch.save(y_test, "y_test.pt")