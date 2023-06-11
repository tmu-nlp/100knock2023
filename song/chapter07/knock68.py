import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from knock67 import vec, target_countries

plt.figure(figsize=(32.0, 24.0))
link = linkage(vec, method='ward')
dendrogram(link, labels=target_countries,leaf_rotation=90,leaf_font_size=10)
plt.show()