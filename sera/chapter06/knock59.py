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

#knock55
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#学習データ
train_cm = confusion_matrix(train["CATEGORY"], train_pred[1])
print(train_cm)
# sns.heatmap(train_cm, annot=True, cmap="Blues")
# plt.show()

#評価データ
test_cm = confusion_matrix(test["CATEGORY"], test_pred[1])
# sns.heatmap(test_cm, annot=True, cmap="Blues")
# plt.show()

#knock56
from sklearn.metrics import precision_score, recall_score, f1_score

def calculate_scores(y_true, y_pred):
  #適合率
  precision = precision_score(test["CATEGORY"], test_pred[1], average=None, labels=["b", "e", "t", "m"])
  precision = np.append(precision, precision_score(y_true, y_pred, average="micro"))
  precision = np.append(precision, precision_score(y_true, y_pred, average="macro"))

  #再現率
  recall = recall_score(test["CATEGORY"], test_pred[1], average=None, labels=["b", "e", "t", "m"])
  recall = np.append(recall, recall_score(y_true, y_pred, average="micro"))
  recall = np.append(recall, recall_score(y_true, y_pred, average="macro"))

  #F1スコア
  f1 = f1_score(test["CATEGORY"], test_pred[1], average=None, labels=["b", "e", "t", "m"])
  f1 = np.append(f1, f1_score(y_true, y_pred, average="micro"))
  f1 = np.append(f1, f1_score(y_true, y_pred, average="macro"))

  #結果を結合してデータフレーム化
  scores = pd.DataFrame({"適合率": precision, "再現率": recall, "F1スコア": f1},
                        index=["b", "e", "t", "m", "マイクロ平均", "マクロ平均"])

  return scores

#knock57
features = X_train.columns.values
index = [i for i in range(1, 11)]
for category, coef in zip(lg.classes_, lg.coef_):
  print("カテゴリ " + category)
  best10 = pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=["重要度上位"], index=index).T
  worst10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=["重要度下位"], index=index).T
  print((pd.concat([best10, worst10], axis=0)))

#knock58
result = []
for C in np.logspace(-5, 2, 10, base=10):
  lg = LogisticRegression(random_state=42, max_iter=10000, C=C)
  lg.fit(X_train, train["CATEGORY"])

  train_pred = score_lg(lg, X_train)
  valid_pred = score_lg(lg, X_valid)
  test_pred = score_lg(lg, X_test)

  train_accuracy = accuracy_score(train["CATEGORY"], train_pred[1])
  valid_accuracy = accuracy_score(valid["CATEGORY"], valid_pred[1])
  test_accuracy = accuracy_score(test["CATEGORY"], test_pred[1])

  result.append([C, train_accuracy, valid_accuracy, test_accuracy])

#グラフ出力
# result = np.array(result).T
# plt.plot(result[0], result[1], label="train")
# plt.plot(result[0], result[2], label="valid")
# plt.plot(result[0], result[3], label="test")
# plt.ylim(0, 1.1)
# plt.ylabel("Accuracy")
# plt.xscale ("log")
# plt.xlabel("C")
# plt.legend()
# plt.show()





#knock59
param = {
    'penalty': ["l1", "l2"],
    "C": [0.001, 0.01, 0.1, 1, 10, 100],
}

max_accuracy = 0
max_param = []

for penalty in param["penalty"]:
    for C in param['C']:
        lg = LogisticRegression(penalty=penalty, max_iter=10000, C=C, solver="liblinear", n_jobs=-1, random_state=42)
        lg.fit(X_train, train['CATEGORY'])

        pred = lg.predict(X_test)
        test_accuracy = accuracy_score(test['CATEGORY'], pred)

        if test_accuracy > max_accuracy:
          max_accuracy = test_accuracy
          max_param = [penalty, C]

print(max_accuracy)
print(max_param)


#勾配ブースティング木
from lightgbm import LGBMClassifier
param = {
    "num_leaves": [30],
    'min_child_weight': [15, 20, 25, 30, 35],
}

max_accuracy = 0
max_param = []

for num_leaves in param["num_leaves"]:
    for min_child_weight in param['min_child_weight']:
        gbm = LGBMClassifier(num_leaves=num_leaves, min_child_weight=min_child_weight, n_jobs=-1, random_state=42)
        gbm.fit(X_train, train['CATEGORY'])

        pred = gbm.predict(X_test)
        test_accuracy = accuracy_score(test['CATEGORY'], pred)

        if test_accuracy > max_accuracy:
          max_accuracy = test_accuracy
          max_param = [num_leaves, min_child_weight]

print(max_accuracy)
print(max_param)