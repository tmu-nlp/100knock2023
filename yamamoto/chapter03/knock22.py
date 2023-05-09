import json
import re

with open('jawiki-country.json', 'r') as f:
    for line in f:
        country = json.loads(line)
        if country['title'] == 'イギリス':
            for sentence in country['text'].splitlines():
                if re.match(r'.*Category:.*?\]', sentence):
                    print(re.match(r'.*Category:(.*?)\]', sentence).group(1))