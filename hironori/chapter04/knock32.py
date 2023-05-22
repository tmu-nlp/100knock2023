from knock30 import k30

for dl in k30():
    for d in dl:
        if d['pos'] == '動詞':
            print(d['base'])