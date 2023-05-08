import json
import gzip
import re
jawkiki_country_list=[]
with gzip.open("jawiki-country.json.gz", "r") as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == "イギリス":
            UK_data = data
            break
L = UK_data["text"].split("\n")
for l in L:
    m = re.search("^=", l)
    if m:
        print(l.strip("[= ]"), l.count("=")//2-1)