import json
import gzip
import re
with gzip.open("jawiki-country.json.gz", "r") as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == "イギリス":
            UK_data = data
            break
L = UK_data["text"].split("\n")

fundamental_info = re.search("{{基礎情報[\s\S]*?}}\n\n", UK_data["text"]).group()

fundamental_info = fundamental_info.split("\n|")
code_regex = re.compile("['\[\]\|\{\{.*?\}\}:.*?:]")
D = dict()
for s in fundamental_info:

    k = re.search("^.*=" ,s)
    v = re.search("=[\s\S]*?$", s)
    if k and v:
        D[re.sub('<.*?>', '', code_regex.sub('', k.group()))[:-2]] = re.sub('<.*?>', '', code_regex.sub('', v.group())[2:])
for k in D:
    print(k)
    print(D[k])