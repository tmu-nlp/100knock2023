from knock51 import vectorizer
import numpy as np
from knock52 import clf
from knock53 import dic


names = np.array(vectorizer.get_feature_names_out())
labels=['b','t','e','m']
for c, coef in zip(clf.classes_, clf.coef_): # カテゴリ毎に表示する
    idx = np.argsort(coef)[::-1]
    print (dic[c])
    print (names[idx][:10]) # 重みの高い特徴量トップ10
    print (names[idx][-10:][::-1]) # 重みの低い特徴量トップ10
