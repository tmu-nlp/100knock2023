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
code_regex = re.compile('[:|*Category\[\]]')
for l in L:
    m = re.search("Category", l)
    if m:
        print(code_regex.sub('', l))