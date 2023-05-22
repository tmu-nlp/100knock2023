from knock30 import knock30
import collections
import numpy as np
import matplotlib.pyplot as plt
DListList = knock30()
V=[]
for DList in DListList:
    for D in DList:
        V.append(D["base"])
c = collections.Counter(V)

best = (c.most_common())
print([d[1] for d in best])
x = np.array([d[1] for d in best])
print(np.array([d[1] for d in best]))
plt.hist(x)
plt.show()