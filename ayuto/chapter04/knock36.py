from knock30 import knock30
import collections
import numpy as np
import matplotlib.pyplot as plt

DListList = knock30()
V=[]
for DList in DListList:
    for D in DList:
        V.append(D["surface"])
c = collections.Counter(V)

best10 = (c.most_common()[:10])
left = np.array([d[0] for d in best10])
height = np.array([d[1] for d in best10])
plt.bar(left, height)
plt.show()