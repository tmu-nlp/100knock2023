# knock51

import pandas as pd
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# 前処理（1.句読点など(具体的には!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.)を除く 2.小文字に統一する 3.数字を取り除く
def preprocessing(text):
    text = "".join([i for i in text if i not in string.punctuation])
    text = text.lower()
    text = re.sub("[0-9]+", "", text)
    return text

# ファイルをdf形式で読み込む
train = pd.read_csv("train.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
valid = pd.read_csv("valid.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])
test = pd.read_csv("test.txt", sep="\t", header=None, names=["TITLE", "CATEGORY"])

# データを連結して前処理
df = pd.concat([train, valid, test], axis=0)
df.reset_index(drop=True, inplace=True)
df["TITLE"] = df["TITLE"].map(preprocessing)

# データを分割
train_valid = df[:len(train) + len(valid)]
test = df[len(train) + len(valid):]
# 単語ベクトル化する
vec_tfidf = TfidfVectorizer()
# tf-idf行列を出力し、DFに変換する  fitで語彙の獲得・idfの計算  transformでtf-idf行列への変換
X_train_valid = vec_tfidf.fit_transform(train_valid["TITLE"])
X_test = vec_tfidf.transform(test["TITLE"]) # transformのみ
X_train_valid = pd.DataFrame(X_train_valid.toarray(), columns=vec_tfidf.get_feature_names_out())
X_test = pd.DataFrame(X_test.toarray(), columns=vec_tfidf.get_feature_names_out())
# 分割
X_train = X_train_valid[:len(train)]
X_valid = X_train_valid[len(train):]

# データを保存
X_train.to_csv('train.feature.txt', sep='\t', index=False)
X_valid.to_csv('valid.feature.txt', sep='\t', index=False)
X_test.to_csv('test.feature.txt', sep='\t', index=False)
