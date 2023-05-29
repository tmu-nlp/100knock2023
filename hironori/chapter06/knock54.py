import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from knock51 import preprc, read_file
from knock53 import score

'''
def preprc(data):
    x = []
    y = []
    label = {"b":0, "e":1, "t":2, "m":3} #ビジネス:0, エンターテインメント:1, 科学技術:2, 健康:3
    for l in data:
        d = l.split("\t")
        x.append(re.sub("[0-9]+", "0", d[1]).lower()) # titleを数字をすべて0、アルファベットを小文字にする
        y.append(label[d[0]])
    return x, y

def read_file():
    train = []
    valid = []
    test = []
    with open('train.txt', encoding='utf-8') as f:
        for l in f:
            train.append(l)
    with open('valid.txt', encoding='utf-8') as f:
        for l in f:
            valid.append(l)
    with open('test.txt', encoding='utf-8') as f:
        for l in f:
            test.append(l)
    return train, valid, test
    
def score(m, x):
    prd = m.predict([x])
    prd_prb = m.predict_proba([x])[0, prd]
    return prd[0], prd_prb[0]
'''

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
    train_acc = accuracy_score(Y_train, train_prd) # 予測結果と正解を比較
    test_acc = accuracy_score(Y_test, test_prd)
    print("学習データの正解率：", train_acc)
    print("評価データの正解率：", test_acc)