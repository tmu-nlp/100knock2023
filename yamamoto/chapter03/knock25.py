import json
import re

with open('jawiki-country.json', 'r') as f:
    for line in f:
        country = json.loads(line)
        if country['title'] == 'イギリス':
            info = re.search(r'\{\{基礎情報.*\n\}\}', country['text'], re.DOTALL+re.MULTILINE).group()
            dictionary = dict(re.findall(r'\|(.*?)=(.*?)\n', info, re.DOTALL))
            print(dictionary)