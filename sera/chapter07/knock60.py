from gensim.models import KeyedVectors

GN_data = KeyedVectors.load_word2vec_format("./chapter07/GoogleNews-vectors-negative300.bin.gz", binary=True)

print(GN_data["United_States"])