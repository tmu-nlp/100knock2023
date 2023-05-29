#knock51

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
# 前処理を適用
train["TITLE"] = train["TITLE"].map(preprocessing)
valid["TITLE"] = valid["TITLE"].map(preprocessing)
test["TITLE"] = test["TITLE"].map(preprocessing)

# 単語ベクトル化する
vec_tfidf = TfidfVectorizer()
# tf-idf行列を出力し、DFに変換する  fitで語彙の獲得、idfの計算  transformでtf-idf行列への変換
X_train = vec_tfidf.fit_transform(train["TITLE"])
X_train = pd.DataFrame(X_train.toarray(), columns=vec_tfidf.get_feature_names_out())
X_valid = vec_tfidf.fit_transform(valid["TITLE"])
X_valid = pd.DataFrame(X_valid.toarray(), columns=vec_tfidf.get_feature_names_out())
X_test = vec_tfidf.fit_transform(test["TITLE"])
X_test = pd.DataFrame(X_test.toarray(), columns=vec_tfidf.get_feature_names_out())

X_train.to_csv('train.feature.txt', sep='\t', index=False)
X_valid.to_csv('valid.feature.txt', sep='\t', index=False)
X_test.to_csv('test.feature.txt', sep='\t', index=False)
