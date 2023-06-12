'''
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

linkage_r = linkage(cs_v, method='ward')

plt.figure(figsize=(16, 9))
dendrogram(linkage_r, labels=cs)
plt.savefig('k68.png')
plt.show()
'''