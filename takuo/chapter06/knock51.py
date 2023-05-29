import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import pandas as pd


def preprocess(txt):
    '''英字とスペース以外(記号，数字など)を削除，小文字化'''
    subed = re.sub(r"[^ a-zA-Z]+", '', txt)
    return subed.lower()


trainfile = os.path.dirname(__file__)+"/train.txt"
train_feat = os.path.dirname(__file__)+"/train.feature.txt"
validfile = os.path.dirname(__file__)+"/valid.txt"
valid_feat = os.path.dirname(__file__)+"/valid.feature.txt"
testfile = os.path.dirname(__file__)+"/test.txt"
test_feat = os.path.dirname(__file__)+"/test.feature.txt"


title_union = []  # title全まとめ
class_train = []  # ラベル格納リスト
class_valid = []
class_test = []
valid_count = 0
train_count = 0
with open(validfile, 'r') as f:
    print(f"readnig:{validfile}.")
    lines = f.readlines()
    valid_count = len(lines)
    for line in lines:
        splted = line.split('\t')
        title_union.append(preprocess(splted[1]))
        class_valid.append(ord(splted[0]))
with open(trainfile, 'r') as f:
    print(f"readnig:{trainfile}.")
    lines = f.readlines()
    train_count = len(lines)
    for line in lines:
        splted = line.split('\t')
        title_union.append(preprocess(splted[1]))
        class_train.append(ord(splted[0]))


# testは含めない．後々学習用データをもとにしたvectornizerでベクトル化する．
title_test = []
with open(testfile, 'r') as f:
    print(f"readnig:{testfile}.")
    for line in f.readlines():
        splted = line.split('\t')
        title_test.append(preprocess(splted[1]))
        class_test.append(ord(splted[0]))


vectornizer = TfidfVectorizer()
title_wordvec_union = vectornizer.fit_transform(title_union).toarray()
title_wordvec_valid = title_wordvec_union[:valid_count]
title_wordvec_train = title_wordvec_union[valid_count:]
title_wordvec_test = vectornizer.transform(title_test).toarray()

if __name__=="__main__":
    with open(train_feat, 'w') as out:
        for idx in range(len(title_wordvec_train)):
            float_stred = [str(float(item)) for item in title_wordvec_train[idx]]
            out.write(str(class_train[idx])+'\t'+','.join(float_stred)+'\n')
    with open(valid_feat, 'w') as out:
        for idx in range(len(title_wordvec_valid)):
            float_stred = [str(float(item)) for item in title_wordvec_valid[idx]]
            out.write(str(class_valid[idx])+'\t'+','.join(float_stred)+'\n')
    with open(test_feat, 'w') as out:
        for idx in range(len(title_wordvec_test)):
            float_stred = [str(float(item)) for item in title_wordvec_test[idx]]
            out.write(str(class_test[idx])+'\t'+','.join(float_stred)+'\n')
