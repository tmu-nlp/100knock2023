import knock30
from knock30 import result

dic = {}  #辞書
d = ""  #文字列

for words in result:
    for a in words:
        if a['pos'] == '名詞':
            d += a['surface']  #名詞を追加
        else:
           dic[d] = len(d)
           d = ''

print([k for k, v in dic.items() if v == max(dic.values())])  #dic:d dの長さ
