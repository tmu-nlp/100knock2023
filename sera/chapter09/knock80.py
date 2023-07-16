import pandas as pd
from sklearn.model_selection import train_test_split
from collections import defaultdict
import string

df = pd.read_csv("./newsCorpora.csv", header=None, sep="\t", names=["ID", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"])

df = df.loc[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]), ["TITLE", "CATEGORY"]]

train, valid_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=123, stratify=df["CATEGORY"])
valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True, random_state=123, stratify=valid_test["CATEGORY"])


# 単語の頻度集計
d = defaultdict(int)
table = str.maketrans(string.punctuation, " "*len(string.punctuation)) # 記号をスペースに変換
for text in train["TITLE"]:
  for word in text.translate(table).split():
    d[word] += 1
d = sorted(d.items(), key=lambda x:x[1], reverse=True)

# 単語ID辞書の作成
word2id = {word: i + 1 for i, (word, cnt) in enumerate(d) if cnt > 1}  # 出現頻度が2回以上の単語を登録

print(f"ID数: {len(set(word2id.values()))}\n")
print("頻度上位10語を表示")
for key in list(word2id)[:10]:
    print(f"{key}: {word2id[key]}")

def tokenizer(text, word2id=word2id, unk=0):
  """ 入力テキストをスペースで分割しID列に変換(辞書になければunkで指定した数字を設定)"""
  table = str.maketrans(string.punctuation, " "*len(string.punctuation))
  return [word2id.get(word, unk) for word in text.translate(table).split()]

# 確認
text = train.iloc[1, train.columns.get_loc("TITLE")]
print(f"テキスト: {text}")
print(f"ID列: {tokenizer(text)}")