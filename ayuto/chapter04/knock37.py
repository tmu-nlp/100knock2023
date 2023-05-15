from knock30 import knock30
import collections
import numpy as np
import matplotlib.pyplot as plt
DListList = knock30()
V=[]
for i in range(len(DListList)):
    for j in range(len(DListList[i])):
        if DListList[i][j]["surface"] == "猫":
            for a in DListList[i]:
                V.append(a["base"])
c = collections.Counter(V)
best10 = (c.most_common()[:11])
print(best10)
left = np.array([d[0] for d in best10])
height = np.array([d[1] for d in best10])
plt.bar(left, height)
plt.show()