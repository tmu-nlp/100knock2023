import sys
import json
import re

args = sys.argv

country_wiki ={}

with open(args[1]) as f:
    for l in f.readlines():
        country_wiki[json.loads(l)["title"]] = json.loads(l)["text"]

#type(article_UK) : <class 'str'>
article_UK = country_wiki["イギリス"]

#\[\[ファイル:(.*\.jpg)
media = re.findall(r'\[\[ファイル:(.+?)\|', article_UK)

for i in range(len(media)):
    print(media[i])