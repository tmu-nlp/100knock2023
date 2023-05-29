# knock54

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ファイルをdf形式で読み込む
train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
test = pd.read_csv("test.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
X_train = pd.read_csv("train.feature.txt", sep="\t")
X_valid = pd.read_csv("valid.feature.txt", sep="\t")
X_test = pd.read_csv("test.feature.txt", sep="\t")

model = LogisticRegression(max_iter=10000)
model.fit(X_train, train["CATEGORY"])

pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

train_accuracy = accuracy_score(train["CATEGORY"], pred_train)
test_accucacy = accuracy_score(test["CATEGORY"], pred_test)
print(train_accuracy)
print(test_accucacy)