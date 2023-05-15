import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for l in f:
        d = json.loads(l)
        if d['title'] == 'イギリス':
            data = d['text']
            break

ls = data.split('\n')
p = r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]' #[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
for l in ls:
    se = re.search(p,l)
    if se:
        print(se[2])
