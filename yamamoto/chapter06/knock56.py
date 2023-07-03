# knock56

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

# ファイルをdf形式で読み込む

train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
X_train = pd.read_csv("train.feature.txt", sep="\t")

model = LogisticRegression()
model.fit(X_train, train["CATEGORY"])

pred_test = model.predict(X_test)

# 適合率、再現率、F1スコアの計算
precision = precision_score(test['CATEGORY'], pred_test, average=None, labels=['b', 'e', 't', 'm'])
precision = np.append(precision, precision_score(test['CATEGORY'], pred_test, average='micro'))
precision = np.append(precision, precision_score(test['CATEGORY'], pred_test, average='macro'))
recall = recall_score(test['CATEGORY'], pred_test, average=None, labels=['b', 'e', 't', 'm'])
recall = np.append(recall, recall_score(test['CATEGORY'], pred_test, average='micro'))
recall = np.append(recall, recall_score(test['CATEGORY'], pred_test, average='macro'))
f1 = f1_score(test['CATEGORY'], pred_test, average=None, labels=['b', 'e', 't', 'm'])
f1 = np.append(f1, f1_score(test['CATEGORY'], pred_test, average='micro'))
f1 = np.append(f1, f1_score(test['CATEGORY'], pred_test, average='macro'))

scores = pd.DataFrame({'適合率': precision,'再現率':recall,'F1スコア':f1},index=['b','e','t','m','マイクロ平均','マクロ平均'])
print(scores)