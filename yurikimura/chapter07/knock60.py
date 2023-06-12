'''
60. 単語ベクトルの読み込みと表示
Google Newsデータセット（約1,000億単語）での学習済み単語ベクトル（300万単語・フレーズ，300次元）をダウンロードし，
”United States”の単語ベクトルを表示せよ．ただし，”United States”は内部的には”United_States”と表現されていることに注意せよ．
'''

from gensim.models import KeyedVectors

#gensimは文書をベクトル化できるPythonのライブラリ
#.wv.save_word2vec_format()で保存された分散表現は，KeyedVectors.load_word2vec_format(ファイルパス)で読み込める
#バイナリファイルを読み込む
model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)
print(model["United_States"])
