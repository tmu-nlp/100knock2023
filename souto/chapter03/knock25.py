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



pattern = r'^\{\{基礎情報.*?^\}\}'
result = '\n'.join(re.findall(pattern, text, re.MULTILINE + re.DOTALL))
pattern = r'^\|.*?\=.*?$'
result = re.findall(pattern, result, re.MULTILINE)

ansdict={}

for i in result:
    kari=i.split('=')
    key=kari[0].strip('|')
    key=key.strip()
    val=kari[1].strip()
    ansdict[key]=val

print(ansdict)
