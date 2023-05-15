import json

with open('jawiki-country.json', 'r') as f:
    for line in f:
        country = json.loads(line)
        if country['title'] == 'イギリス':
            for sentence in country['text'].splitlines():
                if '[[Category' in sentence:
                    print(sentence)