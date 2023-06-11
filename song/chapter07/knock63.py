import gensim
from knock60 import model

model.most_similar(positive=['Spain','Athens'], negative=['Madrid'],topn=10)
