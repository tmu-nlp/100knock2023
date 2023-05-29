import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from knock51 import preprc

train = []
with open('train.txt', encoding='utf-8') as f:
    for l in f:
        train.append(l)
X_train, Y_train = preprc(train)
tfidfvectorizer = TfidfVectorizer(min_df=0.001)
X_train = tfidfvectorizer.fit_transform(X_train).toarray()
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)