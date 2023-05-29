'''
学習データ，検証データ，評価データから特徴量を抽出し，それぞれ
train.feature.txt，valid.feature.txt，test.feature.txtというファイル名で保存せよ．
なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．
記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう．
'''
import string, re, pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#前処理
def preprocessing(text):
    ps = PorterStemmer()
    table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    text = text.translate(table)  # 記号をスペースに置換
    text = text.lower() # 小文字化
    text = re.sub(r"\d+", "0", text)#数値表現を0など特定の数値に置き換える
    text = ps.stem(text) # ステミング
    return text

if __name__ == "__main__":
    #読み込んでDataFrameに変換
    train_df = pd.read_csv("train.csv")
    valid_df = pd.read_csv("valid.csv")
    test_df = pd.read_csv("test.csv")

    #TITLEから予測を行うからTITLEの対して前処理
    #pandasオブジェクトの行や列に対して関数を適用するときはapply()
    train_df["TITLE"] = train_df["TITLE"].apply(preprocessing)
    valid_df["TITLE"] = valid_df["TITLE"].apply(preprocessing)
    test_df["TITLE"] = test_df["TITLE"].apply(preprocessing)

    #特徴量はTF-IDFを使う
    #TF:文書における指定単語の出現頻度
    #IDF:指定単語のレア度（逆文書頻度）
    #TFIDF=TF*IDF

    #オプションのデフォルト:norm=’l2’, use_idf=True, smooth_idf=True, sublinear_tf=False
    vectorizer = TfidfVectorizer()

    vectorizer.fit(train_df["TITLE"])

    #fitで得た語彙からtf-idf行列に変換(scipy.sparse._csr.csr_matrix -> array)
    train_tfidf = vectorizer.transform(train_df["TITLE"]).toarray()
    valid_tfidf = vectorizer.transform(valid_df["TITLE"]).toarray()
    test_tfidf = vectorizer.transform(test_df["TITLE"]).toarray()

    #それぞれDataframeに変換してから保存
    pd.DataFrame(data=train_tfidf).to_csv("train_features.csv", index=False)
    pd.DataFrame(data=valid_tfidf).to_csv("valid_features.csv", index=False)
    pd.DataFrame(data=test_tfidf).to_csv("test_features.csv", index=False)

    #knock57用に[単語]=単語idになる辞書をvocablary_から取得
    with open("vocabulary.pkl", "wb") as f:
        pickle.dump(vectorizer.vocabulary_, f)
