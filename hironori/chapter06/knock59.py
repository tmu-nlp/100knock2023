import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
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
    acs = []
    for c in np.logspace(0, 1, num=5): # 0から10までの値を対数スケールで等間隔に生成
        model = LogisticRegression(C=c, max_iter=1000)
        model.fit(X_train, Y_train)
        test_prd = []
        for x in X_test:
            test_prd.append(score(model, x)[0])
        test_ac = accuracy_score(Y_test, test_prd)
        acs.append(test_ac)
    for m in np.logspace(1, 5, num=5, base=2):
        clf = RandomForestClassifier(max_depth=int(m), random_state=0)
        clf.fit(X_train, Y_train)
        acs.append(accuracy_score(Y_test, clf.predict(X_test)))
    bestidx = acs.index(max(acs))
    if bestidx < 5:
        bestalg = "LogisticRegression"
        bestprm = f"C={np.logspace(0, 1, num=5)[bestidx]}"
    else:
        bestalg = "RandomForestClassifier"
        bestprm = f"max_depth={int(np.logspace(1, 5, num=5, base=2)[bestidx-5])}"
    print(bestalg, bestprm, "正解率：", max(acs))