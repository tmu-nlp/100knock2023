import matplotlib.pyplot as plt
from knock30 import k30

cnt = {}
for dl in k30():
    if any('猫' in d.values() for d in dl):
        dl = [d for d in dl if not any(v == '猫' for v in d.values())]
        for d in dl:
            s = d['base']
            cnt[s] = cnt.get(s, 0) + 1
srt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
l = [t[0] for t in srt[0:10]]
h = [t[1] for t in srt[0:10]]
plt.bar(l, h)