'''
63. 加法構成性によるアナロジー
“Spain”の単語ベクトルから”Madrid”のベクトルを引き，
”Athens”のベクトルを足したベクトルを計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''
from gensim.models import keyedvectors

model = keyedvectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)

# Word2Vec.most_similar(positive=[], negative=[], topn=10, restrict_vocab=None, indexer=None)
# Find the top-N most similar words. Positive words contribute positively towards the similarity, negative words negatively.
# https://tedboy.github.io/nlps/generated/generated/gensim.models.Word2Vec.most_similar.html

print(model.most_similar(positive=["Spain", "Athens"], negative=["Madrid"], topn=10))
