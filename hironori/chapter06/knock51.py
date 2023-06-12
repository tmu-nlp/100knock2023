import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer # データをtf-idfベクトル化

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

if __name__ == "__main__": 
    train, valid, test = read_file()
    X_train, Y_train = preprc(train)
    X_valid, Y_valid = preprc(valid)
    X_test, Y_test = preprc(test)
    tfidfvectorizer = TfidfVectorizer(min_df=0.001)
    X_train = tfidfvectorizer.fit_transform(X_train).toarray()
    X_valid = tfidfvectorizer.transform(X_valid).toarray()
    X_test = tfidfvectorizer.transform(X_test).toarray()
    X_train = pd.DataFrame(X_train, columns = tfidfvectorizer.get_feature_names_out())
    X_valid = pd.DataFrame(X_valid, columns = tfidfvectorizer.get_feature_names_out())
    X_test = pd.DataFrame(X_test, columns = tfidfvectorizer.get_feature_names_out())
    X_train.to_csv("train.feature.txt", sep="\t", index=False)
    X_valid.to_csv("valid.feature.txt", sep="\t", index=False)
    X_test.to_csv("test.feature.txt", sep="\t", index=False)