import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from knock51 import preprc, read_file
from knock53 import score

if __name__ == "__main__":
    train, valid, test = read_file()
    X_train, Y_train = preprc(train)
    X_test, Y_test = preprc(test)
    tfidfvectorizer = TfidfVectorizer(min_df=0.001)
    X_train = tfidfvectorizer.fit_transform(X_train).toarray()
    X_test = tfidfvectorizer.transform(X_test).toarray()
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)
    train_prd = [] # 予測結果をリストに入れる
    test_prd = []
    for x in X_train:
        train_prd.append(score(model, x)[0])
    for x in X_test:
        test_prd.append(score(model, x)[0])
    train_mx = confusion_matrix(Y_train, train_prd)
    sns.heatmap(train_mx, annot=True, cmap="hot_r")
    plt.show()
    test_mx = confusion_matrix(Y_test, test_prd)
    sns.heatmap(train_mx, annot=True, cmap="hot_r")
    plt.show()