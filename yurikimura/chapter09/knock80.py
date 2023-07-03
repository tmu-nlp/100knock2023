'''
80. ID番号への変換Permalink
問題51で構築した学習データ中の単語にユニークなID番号を付与したい．
学習データ中で最も頻出する単語に1，2番目に頻出する単語に2，……といった方法で，
学習データ中で2回以上出現する単語にID番号を付与せよ．そして，与えられた単語列に対して，
ID番号の列を返す関数を実装せよ．
ただし，出現頻度が2回未満の単語のID番号はすべて0とせよ．
'''

# Colab
# https://colab.research.google.com/drive/1CDF6ds6FzLyrZvsEMQ05PYMHRIY5Evgz?usp=sharing


from collections import defaultdict
import string
import pandas as pd
from sklearn.model_selection import train_test_split

def make_train_valid_test(df):
    # データの分割
    train, valid_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=123, stratify=df['CATEGORY'])
    valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True, random_state=123, stratify=valid_test['CATEGORY'])
    train.reset_index(drop=True, inplace=True)
    valid.reset_index(drop=True, inplace=True)
    test.reset_index(drop=True, inplace=True)

    return train, valid, test

def make_word2id_dictionary(text_list):
    # 単語の頻度集計
    d = defaultdict(int)
    table = str.maketrans(string.punctuation, ' '*len(string.punctuation))  # 記号をスペースに置換するテーブル
    for text in text_list:
        for word in text.translate(table).split():
            d[word] += 1
    d = sorted(d.items(), key=lambda x:x[1], reverse=True)

    # 頻度から単語ID辞書の作成
    word2id = {word: i + 1 for i, (word, cnt) in enumerate(d) if cnt > 1}  # 出現頻度が2回以上の単語を登録
    return word2id

def tokenizer(text, word2id, unk=0):
  """ 入力テキストをスペースで分割しID列に変換(辞書になければunkで指定した数字を設定)"""
  table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
  return [word2id.get(word, unk) for word in text.translate(table).split()]


# csvの読み込み
df = pd.read_csv('./newsCorpora.csv', header=None, sep='\t', quoting=3, names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

# データの抽出
df = df.loc[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), ['TITLE', 'CATEGORY']]

train, valid, test = make_train_valid_test(df)
word2id = make_word2id_dictionary(train['TITLE'])

# 確認
text = train.iloc[1, train.columns.get_loc('TITLE')]
id_list = tokenizer(text, word2id)

print(f'テキスト: {text}')
print(f'ID列: {id_list}')
