#できませんでした
import json
import re

with open('jawiki-country.json', 'r') as f:
    for line in f:
        country = json.loads(line)
        if country['title'] == 'イギリス':
            if re.search(r'\{\{基礎情報', country['text']):
                info_start = re.search(r'\{\{基礎情報.*', country['text']).start()
                info_end = re.search(r'.*\}\}', country['text'][info_start:]).end()
                info_string = country['text'][info_start:info_end]
                dict = {}
                for item in info_string.splitlines():
                    if re.match(r'\|(.*)=(.*)', item):
                        dict[re.match(r'\|(.*?)=(.*)', item).group(1)] = re.match(r'\|(.*?)=(.*)', item).group(2)
                print(dict)