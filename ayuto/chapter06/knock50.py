<<<<<<< HEAD
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# ID  TITLE URL PUBLISHER CATEGORY STORY HOSTNAME TIMESTAMP
df = pd.read_table("newsCorpora.csv", names=("ID",  "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"))
target = ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
df = df[df["PUBLISHER"].isin(target)]
train, valid_test = train_test_split(df, test_size=0.2)
valid, test = train_test_split(valid_test, test_size=0.5)

train.to_csv("train.txt", sep="\t", index=False)
valid.to_csv("valid.txt", sep="\t", index=False)
test.to_csv("test.txt", sep="\t", index=False)
print(len(train), len(valid), len(test))
=======
import random
S=[]
with open(r"C:\Users\Ayuto\Downloads\NewsAggregatorDataset (1)\newsCorpora.csv", "r", encoding="utf-8") as f:
    while True:
        try:
            L= f.readline()
            L.split("\t")[3] in ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
            S.append(L)
        except:
            break
random.shuffle(S)
#print(S)
train = S[:int(len(S)*(0.8))]
valid = S[int(len(S)*(0.8)):int(len(S)*(0.9))]
test = S[int(len(S)*(0.9)):]
with open("train.txt", "w", encoding="utf-8") as f:
    f.write("".join(train))
with open("valid.txt", "w", encoding="utf-8") as f:
    f.write("".join(valid))
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("".join(test))
>>>>>>> 5f0664506d2ef51f58972af79ad4b65e854542eb
