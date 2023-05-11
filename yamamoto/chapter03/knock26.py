import json
import re

with open('jawiki-country.json', 'r') as f:
    for line in f:
        country = json.loads(line)
        if country['title'] == 'イギリス':
            info = re.search(r'\{\{基礎情報.*\n\}\}', country['text'], re.DOTALL).group()
            dictionary = dict(re.findall(r'\|(.*?)=(.*?)\n', info, re.DOTALL))
            for k, v in dictionary.items():
                dictionary[k] = re.sub(r'\'{2,5}', '', v)
            print(dictionary)