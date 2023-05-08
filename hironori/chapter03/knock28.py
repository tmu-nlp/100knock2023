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
        p3 = r'\[\[(?:[^|]*?\|)??((?!Category:)([^|]*?))\]\]'
        p4 = r'\{\{lang(?:[^|]*?\|)*?([^|]*?)\}\}' #{{lang|言語タグ|文字列}}
        p5 = r'\[https?://(?:[^\s]*?\s)?([^]]*?)\]' #[https://www.example.org 表示文字], [https://www.example.org]
        p6 = r'<.+?>' #<tag>
        a = re.sub(p6, '', re.sub(p5, r'\1', re.sub(p4, r'\1', re.sub(p3, r'\1', re.sub(p2, r'\2', se[2])))))
        d[se[1]] = a
print(d)
