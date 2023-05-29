#knock50

import pandas as pd
from sklearn.model_selection import train_test_split
# FORMAT: ID \t TITLE \t URL \t PUBLISHER \t CATEGORY \t STORY \t HOSTNAME \t TIMESTAMP
df = pd.read_csv("newsCorpora.csv", sep="\t", header=None, names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

# 該当するpublisherの記事を抽出する
publishers = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
df = df[df['PUBLISHER'].isin(publishers)]
# TITLEとCATEGORYのみ抽出
df = df[["TITLE", "CATEGORY"]]

#データを分割しシャッフルする
train, test = train_test_split(df, test_size=0.2, shuffle=True)
test, valid = train_test_split(test, test_size=0.5, shuffle=True)

#ファイルに保存する
train.to_csv("train.txt", sep="\t", index=False, header=None)
valid.to_csv("valid.txt", sep="\t", index=False, header=None)
test.to_csv("test.txt", sep="\t", index=False, header=None)

print("train\n", train["CATEGORY"].value_counts())
print("valid\n", valid["CATEGORY"].value_counts())
print("test\n", test["CATEGORY"].value_counts())