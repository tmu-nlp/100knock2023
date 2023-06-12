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



pattern = r'(?:\[\[ファイル:)(.*?)(?:\|)'
result = '\n'.join(re.findall(pattern, text))
print(result)

