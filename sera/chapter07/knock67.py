from gensim.models import KeyedVectors
import numpy as np
from sklearn.cluster import KMeans

GN_data = KeyedVectors.load_word2vec_format("./chapter07/GoogleNews-vectors-negative300.bin.gz", binary=True)

# 国名の取得
countries = set()
with open("./chapter07/knock64.txt") as f:
  for line in f:
    line = line.split()
    if line[0] in ["capital-common-countries", "capital-world"]:
      countries.add(line[2])
    elif line[0] in ["currency", "gram6-nationality-adjective"]:
      countries.add(line[1])
countries = list(countries)

# 単語ベクトルの取得
countries_vec = [GN_data[country] for country in countries]

# k-meansクラスタリング
kmeans = KMeans(n_clusters=5)
kmeans.fit(countries_vec)
for i in range(5):
    cluster = np.where(kmeans.labels_ == i)[0]
    print("cluster", i)
    print(", ".join([countries[k] for k in cluster]))
