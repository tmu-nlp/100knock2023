import json
import gzip
jawkiki_country_list=[]
with gzip.open("jawiki-country.json.gz", "r") as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == "イギリス":
            UK_data = data
            break
print(UK_data)
