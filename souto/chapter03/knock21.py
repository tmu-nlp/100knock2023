import json
import re

filename='jawiki-country.json'

f = open(filename, 'r')

text=''

for l in f:
    l = json.loads(l)  
    if l['title'] == 'イギリス':
        text = l['text']
        break

f.close()

#[]は特別な意味を持つため、\が必要
pattern = r'^(\[\[Category.*)'
result = '\n'.join(re.findall(pattern, text, re.MULTILINE))
print(result)