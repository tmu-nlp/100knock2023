import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\Ayuto\Downloads\NewsAggregatorDataset (1)\newsCorpora.csv", sep="\t", header=None, quoting=3)
df.columns = ["ID","TITLE","URL","PUBLISHER","CATEGORY","STORY","HOSTNAME","TIMESTAMP"]

df = df[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"])]

df = df.sample(frac=1, random_state=0)

train, val_test = train_test_split(df, test_size=0.2)
valid, test = train_test_split(val_test, test_size=0.5)

train.to_csv("train.txt", columns=["TITLE","CATEGORY"], sep="\t", header=None, index=False)
valid.to_csv("valid.txt", columns=["TITLE","CATEGORY"], sep="\t", header=None, index=False)
test.to_csv("test.txt", columns=["TITLE","CATEGORY"], sep="\t", header=None, index=False)