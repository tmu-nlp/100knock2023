import json
import re
import requests

with open('jawiki-country.json', 'r') as f:
    for line in f:
        country = json.loads(line)
        if country['title'] == 'イギリス':
            info = re.search(r'\{\{基礎情報.*\n\}\}', country['text'], re.DOTALL+re.MULTILINE).group()
            dictionary = dict(re.findall(r'\|(.*?)=(.*?)\n', info, re.DOTALL, ))
            for k, v in dictionary.items():
                dictionary[k] = re.sub(r'\'{2,5}', '', v)
                dictionary[k] = re.sub(r'\[\[.*?\|(.*?)\]\]', r'\1', v)
                dictionary[k] = re.sub(r'\[\[(.*?)\]\]', r'\1', v)
                dictionary[k] = re.sub(r'\{\{仮リンク\|.*?\|(.*?)\}\}', r'\1', v)
            # print(dictionary)
S = requests.Session()
file = dictionary['国旗画像'].replace(' ', '_')
params = {'action': 'query',
            'titles': 'File:' + file,
            'format': 'json',
            'prop': 'imageinfo',
            'iiprop': 'url'}
res = S.get('https://www.example.org/w/api.php', params)
data = res.json()
url = data['query']['pages']['-1']['imageinfo'][0]['url']
print(url)