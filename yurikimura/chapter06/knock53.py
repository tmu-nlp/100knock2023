'''
52で学習したロジスティック回帰モデルを用い，
与えられた記事見出しからカテゴリとその予測確率を計算するプログラムを実装せよ．
'''
import pickle
import pandas as pd

if __name__ == "__main__":
    X_test = pd.read_csv("test_features.csv") #各単語の特徴量
    Y_test = pd.read_csv("test.csv")["CATEGORY"]#分類の正解ラベル

    #モデル読み込み
    lr = pickle.load(open("model.pkl", "rb"))#rb:バイナリの読み込み

    #予測
    Y_pred = lr.predict(X_test) #予測結果（カテゴリ）のリスト

    #予測確率を計算
    Y_proba = lr.predict_proba(X_test)#4つのカテゴリに対する予測確率

    accuracy = 0
    #print(f"ID\t予測\t正解\t予測確率")
    for i, pred in enumerate(Y_pred):
        if Y_pred[i] == Y_test[i]:
            accuracy += 1
        y_proba = "{:.3f}".format(max(Y_proba[i]))#小数点以下三桁

    print("accuracy:", float(accuracy/len(Y_test)))
