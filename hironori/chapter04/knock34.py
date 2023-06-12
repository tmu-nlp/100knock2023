from knock30 import k30

ans = []
a = []
for dl in k30():
    i = 0
    while i < len(dl)-1:
        if dl[i]['pos'] == '名詞' and dl[i+1]['pos'] == '名詞':
            a.append(dl[i]['surface'])
            a.append(dl[i+1]['surface'])
            i = i + 1
            if i+1 < len(dl)-1:
                while dl[i+1]['pos'] == '名詞' and i+1 < len(dl)-1:
                    a.append(dl[i+1]['surface'])
                    i = i + 1
            ans.append(a)
            a = []
        i = i+1
print(ans)