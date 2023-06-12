import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

train_df = pd.read_csv("train.txt", sep="\t", header=None)
valid_df = pd.read_csv("valid.txt", sep="\t", header=None)
test_df = pd.read_csv("test.txt", sep="\t", header=None)
colums_name = ["TITLE", "CATEGORY"]
train_df.columns = colums_name
valid_df.columns = colums_name
test_df.columns = colums_name

vectorizer = TfidfVectorizer()

vectorizer.fit(train_df["TITLE"])

train_tfidf = vectorizer.transform(train_df["TITLE"])
valid_tfidf = vectorizer.transform(valid_df["TITLE"])
test_tfidf = vectorizer.transform(test_df["TITLE"])

train_tfidf = train_tfidf.toarray()
valid_tfidf = valid_tfidf.toarray()
test_tfidf = test_tfidf.toarray()

pd.DataFrame(data=train_tfidf).to_csv("train.feature.txt", sep="\t", index=False, header=None)
pd.DataFrame(data=valid_tfidf).to_csv("valid.feature.txt", sep="\t", index=False, header=None)
pd.DataFrame(data=test_tfidf).to_csv("test.feature.txt", sep="\t", index=False, header=None)

with open("vocabulary.pkl", "wb") as f:
    pickle.dump(vectorizer.vocabulary_, f)