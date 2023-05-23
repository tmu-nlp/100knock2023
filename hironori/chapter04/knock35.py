from knock30 import k30

cnt = {}
for dl in k30():
    for d in dl:
        s = d['base']
        cnt[s] = cnt.get(s, 0) + 1
ans = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

print(ans)