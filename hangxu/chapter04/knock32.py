import knock30
from knock30 import result

for sentence in result:
    for a in sentence:
        if a['pos'] == '動詞':
            print(a['base'])