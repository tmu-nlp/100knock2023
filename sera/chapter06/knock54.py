import pandas as pd
from sklearn.model_selection import train_test_split

#データ読み込み
df = pd.read_csv("newsCorpora.csv", header=None, sep="\t", names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

#データ抽出
df = df.loc[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]), ["CATEGORY", "TITLE"]]
df = df.sample(frac=1, ignore_index=True, random_state=42)

#データ分割
train, valid_test = train_test_split(df, test_size=0.2)
valid, test = train_test_split(valid_test, test_size=0.5)

#knock51
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocessing(text):
  table = str.maketrans(string.punctuation, " "*len(string.punctuation))
  text = text.translate(table)  #記号をスペースに置換
  text = text.lower()  #小文字化
  text = re.sub("[0-9]+", "0", text)  #数字列を0に置換

  return text

# 前処理の実施
df["TITLE"] = df["TITLE"].map(lambda x: preprocessing(x))

#データの分割
train_valid = df[:len(train) + len(valid)]
test = df[len(train) + len(valid):]

#TfidfVectorizer
vec_tfidf = TfidfVectorizer(min_df=10, ngram_range=(1, 2))

#ベクトル化
X_train_valid = vec_tfidf.fit_transform(train_valid["TITLE"])
X_test = vec_tfidf.transform(test["TITLE"])

#ベクトルをデータフレームに変換
X_train_valid = pd.DataFrame(X_train_valid.toarray(), columns=vec_tfidf.get_feature_names_out())
X_test = pd.DataFrame(X_test.toarray(), columns=vec_tfidf.get_feature_names_out())

#データの分割
X_train = X_train_valid[:len(train)]
X_valid = X_train_valid[len(train):]

#データの保存
X_train.to_csv("train.feature.txt", sep="\t", index=False)
X_valid.to_csv("valid.feature.txt", sep="\t", index=False)
X_test.to_csv("test.feature.txt", sep="\t", index=False)

#knock52
from sklearn.linear_model import LogisticRegression

#モデルの学習
lg = LogisticRegression(random_state=42, max_iter=10000)
lg.fit(X_train, train["CATEGORY"])

#knock53
import numpy as np

def score_lg(lg, X):
  return [np.max(lg.predict_proba(X), axis=1), lg.predict(X)]

train_pred = score_lg(lg, X_train)
test_pred = score_lg(lg, X_test)

#knock54
from sklearn.metrics import accuracy_score

train_accuracy = accuracy_score(train["CATEGORY"], train_pred[1])
test_accuracy = accuracy_score(test["CATEGORY"], test_pred[1])
print("正解率(訓練データ): {}".format(train_accuracy))
print("正解率(テストデータ): {}".format(test_accuracy))