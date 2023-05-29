import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score # 適合率、再現率、f1スコア
from knock51 import preprc, read_file
from knock53 import score

def k56(y, prd):
    ppv = precision_score(y, prd, average=None)
    ppvmi = precision_score(y, prd, average="micro").reshape(1)
    ppvma = precision_score(y, prd, average="macro").reshape(1)
    ppv = np.concatenate([ppv, ppvmi, ppvma])
    recall = recall_score(y, prd, average=None)
    recallmi = recall_score(y, prd, average="micro").reshape(1)
    recallma = recall_score(y, prd, average="macro").reshape(1)
    recall = np.concatenate([recall, recallmi, recallma])
    f1 = f1_score(y, prd, average=None)
    f1mi = f1_score(y, prd, average="micro").reshape(1)
    f1ma = f1_score(y, prd, average="macro").reshape(1)
    f1 = np.concatenate([f1, f1mi, f1ma])
    idx = ["0", "1", "2", "3", "micro", "macro"]
    scs = pd.DataFrame({"ppv":ppv, "recall":recall, "f1":f1}, index=idx)
    return scs

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
    print(k56(Y_test, test_prd))