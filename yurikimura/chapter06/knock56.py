# knock56
# 52で学習したロジスティック回帰モデルの適合率，再現率，F1スコアを，評価データ上で計測せよ．
# カテゴリごとに適合率，再現率，F1スコアを求め，
# カテゴリごとの性能をマイクロ平均（micro-average）とマクロ平均（macro-average）で統合せよ．
import pickle
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

if __name__ == "__main__":
    X_test = pd.read_csv("test_features.csv")
    Y_test = pd.read_csv("test.csv")["CATEGORY"]

    lr = pickle.load(open("model.pkl", "rb"))

    Y_pred = lr.predict(X_test)

    #適合率,再現率，F1スコアを求める
    #average=Noneにすると各カテゴリを陽性にしたときの値がリストで返される
    labels = ["b","t","e","m"]#ラベルの順序指定
    precision = precision_score(Y_test, Y_pred, average=None, labels=labels)
    recall = recall_score(Y_test, Y_pred, average=None, labels=labels)
    f1 = f1_score(Y_test, Y_pred, average=None, labels=labels)

    #マクロ平均:average=Noneの時のリストの算術平均
    precision_macro = precision_score(Y_test, Y_pred, average="macro")
    recall_macro = recall_score(Y_test, Y_pred, average="macro")
    f1_macro = f1_score(Y_test, Y_pred, average="macro")

    #マイクロ平均:各カテゴリのTP,TN,FP,FNを計算し，全カテゴリまとめてから計算する
    precision_micro = precision_score(Y_test, Y_pred, average="micro")
    recall_micro = recall_score(Y_test, Y_pred, average="micro")
    f1_micro = f1_score(Y_test, Y_pred, average="micro")

    #出力用に桁を指定
    precision = ["{:.3f}".format(value) for value in precision]
    recall = ["{:.3f}".format(value) for value in recall]
    f1 = ["{:.3f}".format(value) for value in f1]

    #出力
    print("カテゴリ :b\tt\te\tm")
    print(f"適合率  :{precision[0]}\t{precision[1]}\t{precision[2]}\t{precision[2]}")
    print(f"再現率  :{recall[0]}\t{recall[1]}\t{recall[2]}\t{recall[2]}")
    print(f"F1スコア:{f1[0]}\t{f1[1]}\t{f1[2]}\t{f1[2]}")

    print("\tマクロ平均\t\tマイクロ平均")
    print(f"適合率  :{precision_macro}\t{precision_micro}")
    print(f"再現率  :{recall_macro}\t{recall_micro}")
    print(f"F1スコア:{f1_macro}\t{f1_micro}")
