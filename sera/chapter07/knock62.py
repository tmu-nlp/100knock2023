from gensim.models import KeyedVectors

GN_data = KeyedVectors.load_word2vec_format("./chapter07/GoogleNews-vectors-negative300.bin.gz", binary=True)

ans = GN_data.most_similar("United_States", topn=10)
print(ans)