import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


X_train = pd.read_table("train.feature.txt", header=None) #各単語の特徴量
Y_train = pd.read_table("train.txt", header=None)[1]#分類の正解ラベル

lr = LogisticRegression(random_state=0, max_iter=1000)
lr.fit(X_train, Y_train)#ロジスティック回帰モデルの重みを学習

with open("model.pkl", "wb") as f:
    pickle.dump(lr, f)