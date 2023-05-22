import matplotlib.pyplot as plt
from knock30 import k30

cnt = {}
for dl in k30():
    for d in dl:
        s = d['base']
        cnt[s] = cnt.get(s, 0) + 1
srt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
y = [t[1] for t in srt]
plt.plot(range(1,len(y)+1), y)
plt.xscale('log')
plt.yscale('log')