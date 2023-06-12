# knock55

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# ファイルをdf形式で読み込む
train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
test = pd.read_csv("test.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
X_train = pd.read_csv("train.feature.txt", sep="\t")
X_valid = pd.read_csv("valid.feature.txt", sep="\t")
X_test = pd.read_csv("test.feature.txt", sep="\t")

model = LogisticRegression(max_iter=10000)
model.fit(X_train, train["CATEGORY"])

pred_train = model.predict(X_train)
train_cm = confusion_matrix(train["CATEGORY"], pred_train)
print(train_cm)

pred_test = model.predict(X_test)
test_cm = confusion_matrix(test["CATEGORY"], pred_test)
print(test_cm)