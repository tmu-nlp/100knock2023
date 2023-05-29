# knock53

from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

# ファイルをdf形式で読み込む
train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
X_train = pd.read_csv("train.feature.txt", sep="\t")
X_valid = pd.read_csv("valid.feature.txt", sep="\t")

model = LogisticRegression(max_iter=10000)
model.fit(X_train, train["CATEGORY"])

pred_category = model.predict(X_valid["TITLE"])
pred_probability = model.predict_proba(X_valid)
print(pred_category)
print(pred_probability)