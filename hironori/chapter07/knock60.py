'''
from google.colab import drive
drive.mount('/content/drive')

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('/content/drive/MyDrive/GoogleNews-vectors-negative300.bin.gz', binary=True)
print(model['United_States'])
'''