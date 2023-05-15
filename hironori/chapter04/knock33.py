from knock30 import k30

for dl in k30():
    for i in range(1, len(dl)-1):
        if dl[i-1]['pos'] == '名詞' and dl[i]['surface'] == 'の' and dl[i+1]['pos'] == '名詞':
            print(dl[i-1]['surface'] + dl[i]['surface'] + dl[i+1]['surface'])