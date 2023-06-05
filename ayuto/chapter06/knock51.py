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
