# knock57

from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

# ファイルをdf形式で読み込む
train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
X_train = pd.read_csv("train.feature.txt", sep="\t")

model = LogisticRegression()
model.fit(X_train, train["CATEGORY"])

# 特徴量を取り出す
features = X_train.columns.values
# cはカテゴリ名、coefは特徴量毎の重み
for c, coef in zip(model.classes_, model.coef_):
    print(f'カテゴリ名：{c}')
    # argsort：ソートして元のインデックスで返す
    # dfにして見やすくしてる（ features[np.argsort(-coef)[:10]] でいい）
    top_10 = pd.DataFrame(features[np.argsort(-coef)[6:10]], columns=["重みの上位10"], index=[i for i in range(1, 11)])
    worst_10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=["重みの下位10"], index=[i for i in range(1, 11)])
    print(top_10)
    print(worst_10)