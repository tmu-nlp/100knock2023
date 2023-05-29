# knock52

from sklearn.linear_model import LogisticRegression
import pandas as pd

# ファイルをdf形式で読み込む
train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
X_train = pd.read_csv("train.feature.txt", sep="\t")

model = LogisticRegression()
model.fit(X_train, train["CATEGORY"])