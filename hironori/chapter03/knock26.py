import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for l in f:
        d = json.loads(l)
        if d['title'] == 'イギリス':
            data = d['text']
            break

ls = data.split('\n')
p = r'\|(.+?)\s=\s*(.+)' 
d = {}
for l in ls:
    se = re.search(p,l)
    if se:
        p2 = r'(\'{2,5})(.*?)(\1)' #''他との区別'', '''強調''', '''''斜体と強調'''''
        a = re.sub(p2, r'\2', se[2])
        d[se[1]] = a
print(d)
