import pickle
import pandas as pd
from sklearn.metrics import confusion_matrix

if __name__ == "__main__":
    X_train = pd.read_csv("train_features.csv")
    Y_train = pd.read_csv("train.csv")["CATEGORY"]
    X_test = pd.read_csv("test_features.csv")
    Y_test = pd.read_csv("test.csv")["CATEGORY"]

    lr = pickle.load(open("model.pkl", "rb"))

    #混同行列を作成
    #b = business, t = science and technology, e = entertainment, m = health
    labels = ["b","t","e","m"]#ラベルの順序指定
    train_cm = confusion_matrix(Y_train, lr.predict(X_train), labels=labels)
    test_cm = confusion_matrix(Y_test, lr.predict(X_test), labels=labels)

    #見やすく出力
    colums_labels = ["pred_" + str(l) for l in labels]
    index_labels = ["act_" + str(l) for l in labels]
    train_cm = pd.DataFrame(train_cm, columns=colums_labels, index=index_labels)
    test_cm = pd.DataFrame(test_cm, columns=colums_labels, index=index_labels)
    print("訓練データの混同行列")
    print(train_cm)
    print("評価データの混同行列")
    print(test_cm)
