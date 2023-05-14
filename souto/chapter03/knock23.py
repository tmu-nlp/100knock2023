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



pattern = r'^(\=+.*?\=+)'
result = '\n'.join(re.findall(pattern, text, re.MULTILINE))
result = result.split('\n')

for i in result:
    eqnum=0
    while i[eqnum]=='=':
        eqnum=eqnum+1
    index=eqnum
    while i[index]==' ':
        index=index+1
    print(f'{i[index:-index]} : {str(eqnum-1)}')