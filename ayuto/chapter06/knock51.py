<<<<<<< HEAD
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

train_df = pd.read_table("train.txt")
test_df = pd.read_table("test.txt")
valid_df = pd.read_table("valid.txt")
tfidf = TfidfVectorizer() # 正規化手法を選択
tfidf.fit(train_df["TITLE"]) # fitで単語ベクトルの空間を定義
train_feature = tfidf.transform(train_df["TITLE"]) # 単語ベクトル化
test_feature = tfidf.transform(test_df["TITLE"])
valid_feature = tfidf.transform(valid_df["TITLE"])


train_tfidf = train_feature.toarray()
valid_tfidf = valid_feature.toarray()
test_tfidf = test_feature.toarray()

pd.DataFrame(data=train_tfidf).to_csv("train.feature.txt", sep="\t", index=False, header=None)
pd.DataFrame(data=valid_tfidf).to_csv("valid.feature.txt", sep="\t", index=False, header=None)
pd.DataFrame(data=test_tfidf).to_csv("test.feature.txt", sep="\t", index=False, header=None)
=======
import re
code_regex = re.compile(r"[()\.[]{},]")
S=[]
with open(r"train.txt", "r", encoding="utf-8") as f:
    while True:
        try:
            L= f.readline()
            L = list(L.split("\t")[1].split(" "))
            #print(L)
            for l in L:
                S.append(code_regex.sub("", l))
        except:
            break
with open("train.feature.txt", "w", encoding="utf-8") as f:
    f.write("\t".join(S))
>>>>>>> 5f0664506d2ef51f58972af79ad4b65e854542eb
