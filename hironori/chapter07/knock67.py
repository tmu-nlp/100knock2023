'''
from sklearn.cluster import KMeans
import numpy as np

c1 = ['capital-common-countries', 'capital-world']
c2 = ['currency', 'gram6-nationality-adjective']
cs = set()
with open('/content/drive/MyDrive/questions-words-ans.txt', encoding='utf-8') as f:
    for r in f:
        cols = r.strip().split('\t')
        if cols[0] in c1:
            country = cols[1].split()[1]
            cs.add(country)
        elif cols[0] in c2:
            country = cols[1].split()[0]
            cs.add(country)
        else:
            continue
cs = list(cs)
#print(len(cs))
#print(cs)

cs_v = [model[country] for country in cs]

kmeans = KMeans(n_clusters=5)
kmeans.fit(cs_v)
for i in range(5):
    cluster = np.where(kmeans.labels_ == i)[0]
    print('cluster', i)
    print(', '.join([cs[k] for k in cluster]))
'''