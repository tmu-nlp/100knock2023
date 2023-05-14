import json

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for l in f:
        d = json.loads(l)
        if d['title'] == 'イギリス':
            data = d['text']
            break

c = list(filter(lambda x: '[Category:' in x, data.split('\n')))
print(c)