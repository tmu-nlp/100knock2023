from knock30 import knock30
import collections
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
DListList = knock30()
V=[]
for i in range(len(DListList)):
    for j in range(len(DListList[i])):
        if DListList[i][j]["surface"] == "猫":
            for a in DListList[i]:
                V.append(a["base"])
c = collections.Counter(V)
best10 = (c.most_common())
print(best10)
left = np.array(range(1, len(best10)+1))
height = np.array([d[1] for d in best10])
plt.scatter(left, height)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.set_yscale('log')  # y軸をlogスケールで描く
ax.set_xscale('log')  # x軸をlogスケールで描く
plt.show()