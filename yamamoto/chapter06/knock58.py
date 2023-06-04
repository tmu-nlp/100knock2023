# knock58

from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

# ファイルをdf形式で読み込む
train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
X_train = pd.read_csv("train.feature.txt", sep="\t")

accuracy = []
# logspace(start,stop,number_of_list,base='底')
for c in np.logspace(-4, 2, 7, base=10):
  # 学習
  model = LogisticRegression(max_iter=10000, C=c)
  model.fit(X_train, train["CATEGORY"])
  # 予測
  pred_train = model.predict(X_train)
  pred_valid = model.predict(X_valid)
  pred_test = model.predict(X_test)
  # 正解率を求める
  train_accuracy = accuracy_score(train['CATEGORY'], pred_train)
  valid_accuracy = accuracy_score(valid['CATEGORY'], pred_valid)
  test_accuracy = accuracy_score(test['CATEGORY'], pred_test)

  accuracy.append([c, train_accuracy, valid_accuracy, test_accuracy])

accuracy = np.array(accuracy).T
plt.plot(accuracy[0], accuracy[1], label='train')
plt.plot(accuracy[0], accuracy[2], label='valid')
plt.plot(accuracy[0], accuracy[3], label='test')
plt.ylabel('Accuracy')
plt.xlabel('C')
plt.xscale('log')
plt.legend()
plt.show()