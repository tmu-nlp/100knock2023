import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from knock51 import preprc, read_file
from knock53 import score
from knock56 import k56

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
    fts = pd.DataFrame(X_train, columns = tfidfvectorizer.get_feature_names_out()).columns.values
    for i, coef in enumerate(model.coef_):
        top = fts[np.argsort(coef)[::-1][:10]]
        worst = fts[np.argsort(coef)[:10]]
        print("クラス：", i) #ビジネス:0, エンターテインメント:1, 科学技術:2, 健康:3
        print("重みの高いトップ10：", top)
        print("重みの低いトップ10：", worst)