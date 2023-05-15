import matplotlib.pyplot as plt
from knock30 import k30

cnt = {}
for dl in k30():
    for d in dl:
        s = d['surface']
        cnt[s] = cnt.get(s, 0) + 1
x = []
for w,i in cnt.items():
    x.append(i)
plt.hist(x, bins=40, range=(1, 41))