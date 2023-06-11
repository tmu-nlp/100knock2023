import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('/home/nevucide/GoogleNews-vectors-negative300.bin', binary=True)
model['United_States']