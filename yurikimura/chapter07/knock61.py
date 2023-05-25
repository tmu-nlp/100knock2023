from gensim.models import keyedvectors

model = keyedvectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)
#similarityでコサイン類似度が求められる
print(model.similarity("United_States", "U.S."))

"""
0.7310774
"""
