import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for l in f:
        d = json.loads(l)
        if d['title'] == 'イギリス':
            data = d['text']
            break

ls = data.split('\n')
p = r'(={2,})(.+?)={2,}' #== Level N == (Nが'='の数)
for l in ls:
    se = re.search(p,l)
    if se:
        print(se[2].strip(), len(se[1])-1)
