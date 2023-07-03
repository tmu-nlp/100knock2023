from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format(r"C:\Users\Ayuto\Downloads\GoogleNews-vectors-negative300.bin.gz",binary=True)
print(model["United_States"])