from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from knock67 import vec, target_countries

vec_embedded = TSNE(n_components=2).fit_transform(vec)
vec_embedded_t = list(zip(*vec_embedded)) # 転置
fig, ax = plt.subplots(figsize=(16, 12))
plt.scatter(*vec_embedded_t)
for i, c in enumerate(target_countries):
    ax.annotate(c, (vec_embedded[i][0],vec_embedded[i][1]))
