import knock50
from knock50 import train
from knock50 import valid
from knock50 import  test

import string
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


#テキストの前処理
def preprocessing(text):
  text = "".join([i for i in text if i not in string.punctuation]) ##マック
  text = text.lower() ##小文字
  text = re.sub("[0-9]+", "", text) ##連続の数字を置換
  return text

text = pd.concat([train, valid, test], axis = 0)
text['TITLE'] = text['TITLE'].map(lambda x: preprocessing(x))

#単語をベクトル化し、DataFrameに変換する
vectorizer = TfidfVectorizer(min_df=10, ngram_range=(1, 2)) ##tf-idf: 各文章の中で各単語の重要度の統計量を示す
X = vectorizer.fit_transform(text['TITLE']).toarray()
X_df = pd.DataFrame(X, columns=vectorizer.get_feature_names_out()) ##.get_feature_names_out:特徴量

#分割する
x_train = X_df.iloc[:len(train), :] ##iloc(行，列): データを輸出する
x_valid = X_df.iloc[len(train):len(train)+ len(valid), :] 
x_test = X_df.iloc[len(train)+ len(valid):, :] 

#ファイルを輸出する
#x_train.to_csv('train.feature.txt', sep='\t', index=False)
#x_valid.to_csv('valid.feature.txt', sep='\t', index=False)
#x_test.to_csv('test.feature.txt', sep='\t', index=False)




