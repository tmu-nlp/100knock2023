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
