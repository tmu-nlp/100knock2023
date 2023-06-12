import pandas as pd
from sklearn.model_selection import train_test_split

#データ読み込み
df = pd.read_csv("newsCorpora.csv", header=None, sep="\t", names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

#データ抽出
df = df.loc[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]), ["CATEGORY", "TITLE"]]
df = df.sample(frac=1, ignore_index=True, random_state=42)

#データ分割
train, valid_test = train_test_split(df, test_size=0.2)
valid, test = train_test_split(valid_test, test_size=0.5)

#データ保存
train.to_csv("train.txt", sep="\t", index=False)
valid.to_csv("./valid.txt", sep="\t", index=False)
test.to_csv("./test.txt", sep="\t", index=False)

#各カテゴリの事例数
print("学習データ")
print(train["CATEGORY"].value_counts())
print("検証データ")
print(valid["CATEGORY"].value_counts())
print("評価データ")
print(test["CATEGORY"].value_counts())