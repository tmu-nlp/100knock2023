import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

if __name__ == "__main__":
    X_train = pd.read_table("train.feature.txt", header=None)
    Y_train = pd.read_table("train.txt", header=None)[1]
    X_test = pd.read_table("test.feature.txt", header=None)
    Y_test = pd.read_table("test.txt", header=None)[1]
    lr = pickle.load(open("model.pkl", "rb"))
    labels = ["b","t","e","m"]
    train_cm = confusion_matrix(Y_train, lr.predict(X_train), labels=labels)
    test_cm = confusion_matrix(Y_test, lr.predict(X_test), labels=labels)
    colums_labels = ["pred_" + str(l) for l in labels]
    index_labels = ["act_" + str(l) for l in labels]
    train_cm = pd.DataFrame(train_cm, columns=colums_labels, index=index_labels)
    test_cm = pd.DataFrame(test_cm, columns=colums_labels, index=index_labels)
    print(train_cm)
    print(test_cm)