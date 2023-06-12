'''
52で学習したロジスティック回帰モデルの正解率を，
学習データおよび評価データ上で計測せよ．
'''
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    X_train = pd.read_csv("train_features.csv")
    Y_train = pd.read_csv("train.csv")["CATEGORY"]
    X_test = pd.read_csv("test_features.csv")
    Y_test = pd.read_csv("test.csv")["CATEGORY"]

    lr = pickle.load(open("model.pkl", "rb"))

    #正解率の計算
    train_ac = accuracy_score(Y_train, lr.predict(X_train))
    test_ac = accuracy_score(Y_test, lr.predict(X_test))

    print(f"学習データの正解率:{train_ac}")
    print(f"評価データの正解率:{test_ac}")
