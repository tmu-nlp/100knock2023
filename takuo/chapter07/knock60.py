import gensim
import os
import pickle

# gensimライブラリを使う．
# word2vecモデルだとバカデカファイルが出来上がるので，KeyedVectorsを使って軽量化(https://radimrehurek.com/gensim/models/keyedvectors.html)

wordvec = gensim.models.KeyedVectors.load_word2vec_format(
    f"{os.path.dirname(__file__)}/GoogleNews-vectors-negative300.bin.gz",
    binary=True)

# with open(f"{os.path.dirname(__file__)}/wordvec.kv", 'wb')as storefile:
#     # 学習モデルを保存(メモリ内容をバイナリでファイルに書き出し)
#     pickle.dump(wordvec, storefile)

# save()で書き出し
# wordvec.save(f"{os.path.dirname(__file__)}/wordvec")
wordvec = gensim.models.KeyedVectors.load(
    f"{os.path.dirname(__file__)}/wordvec.vectors.npy", mmap='r')

print(wordvec.most_similar('Tokyo'))
