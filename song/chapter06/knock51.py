from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from knock50 import train_df, valid_df, test_df

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_df['TITLE'])
X_valid = vectorizer.transform(valid_df['TITLE'])
X_test = vectorizer.transform(test_df['TITLE'])
np.savetxt('./song/chapter06/train.feature.txt', X_train.toarray(), fmt='%d') # スパース行列から密行列に変換
np.savetxt('./song/chapter06/valid.feature.txt', X_valid.toarray(), fmt='%d')
np.savetxt('./song/chapter06/test.feature.txt', X_test.toarray(), fmt='%d')
