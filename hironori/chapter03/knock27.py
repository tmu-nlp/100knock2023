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
        p2 = r'(\'{2,5})(.*?)(\1)'
        p3 = r'\[\[(?:[^|]*?\|)??((?!Category:)([^|]*?))\]\]' #[[記事名]], [[記事名|表示文字]], [[記事名#節名|表示文字]]
        a = re.sub(p3, r'\1', re.sub(p2, r'\2', se[2]))
        d[se[1]] = a
print(d)
