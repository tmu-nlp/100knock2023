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

result = re.sub(r'\'{2,5}', '', result)

pattern = r'\[\[(?:.*?)(\#?.*?\|)?.*?\]\]'#https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8　において記事名だけ残すようにした
result = re.sub(pattern, r'\1', result)

pattern = r'\[.*?\]'#外部リンク
result = re.sub(pattern, '', result)

pattern = r'\#REDIRECT [[.*?]]'#リダイレクト
result = re.sub(pattern, '', result)


pattern = r'<!-- .*? -->'#コメントアウト
result = re.sub(pattern, '', result)

pattern = r'{{(.*?)}}'#テンプレート
result = re.sub(pattern, r'\1', result)

pattern = r'^\|.*?\=.*?$'
result = re.findall(pattern, result, re.MULTILINE)


ansdict={}

for i in result:
    kari=i.split('=')
    key=kari[0].strip('|')
    key=key.strip()
    val=kari[1].strip()
    ansdict[key]=re.sub(r'<ref.*?$', '', val)

for k, v in ansdict.items():
    print(k + ': ' + v.strip('|'))
