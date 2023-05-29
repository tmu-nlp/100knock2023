import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from knock51 import preprc, read_file
from knock53 import score
from knock56 import k56

if __name__ == "__main__":
    train, valid, test = read_file()
    X_train, Y_train = preprc(train)
    X_valid, Y_valid = preprc(valid)
    X_test, Y_test = preprc(test)
    tfidfvectorizer = TfidfVectorizer(min_df=0.001)
    X_train = tfidfvectorizer.fit_transform(X_train).toarray()
    X_valid = tfidfvectorizer.transform(X_valid).toarray()
    X_test = tfidfvectorizer.transform(X_test).toarray()
    r = []
    for c in np.logspace(-2, 2, num=20): # 10^-3から10^2までの値を対数スケールで等間隔に生成
        model = LogisticRegression(C=c, max_iter=1000)
        model.fit(X_train, Y_train)
        train_prd = []
        valid_prd = []
        test_prd = []
        for x in X_train:
            train_prd.append(score(model, x)[0])
        for x in X_valid:
            valid_prd.append(score(model, x)[0])
        for x in X_test:
            test_prd.append(score(model, x)[0])
        train_ac = accuracy_score(Y_train, train_prd)
        valid_ac = accuracy_score(Y_valid, valid_prd)
        test_ac = accuracy_score(Y_test, test_prd)
        r.append([c, train_ac, valid_ac, test_ac])
    r = np.array(r).T
    plt.plot(-np.log10(r[0]), r[1], label="train")
    plt.plot(-np.log10(r[0]), r[2], label="valid")
    plt.plot(-np.log10(r[0]), r[3], label="test")
    plt.ylim(0.5, 1.0)
    plt.xlabel("log λ")
    plt.ylabel("accuracy")
    plt.legend()
    plt.show()