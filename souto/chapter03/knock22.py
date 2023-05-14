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


#(?:  )で反応するがキャプチャしない文字列
pattern = r'^(?:\[\[Category:)(.*?)(?:\|.)?\]\]'
result = '\n'.join(re.findall(pattern, text, re.MULTILINE))
print(result)