import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from knock51 import preprc

def score(m, x):
    prd = m.predict([x])
    prd_prb = m.predict_proba([x])[0, prd]
    return prd[0], prd_prb[0]

if __name__ == "__main__":
    train = []
    test = []
    with open('train.txt', encoding='utf-8') as f:
        for l in f:
            train.append(l)
    with open('test.txt', encoding='utf-8') as f:
        for l in f:
            test.append(l)
    X_train, Y_train = preprc(train)
    X_test, Y_test = preprc(test)
    tfidfvectorizer = TfidfVectorizer(min_df=0.001)
    X_train = tfidfvectorizer.fit_transform(X_train).toarray()
    X_test = tfidfvectorizer.transform(X_test).toarray()
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)

    for i in range(20):
        print(score(model, X_test[i]))