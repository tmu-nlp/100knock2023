import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for l in f:
        d = json.loads(l)
        if d['title'] == 'イギリス':
            data = d['text']
            break

ls = data.split('\n')
p = '\|(.+?)\s=\s*(.+)' #ex.|略名 = イギリス\n
d = {}
for l in ls:
    se = re.search(p,l)
    if se:
        d[se[1]] = se[2]
print(d)
