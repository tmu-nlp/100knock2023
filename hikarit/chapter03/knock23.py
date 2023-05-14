import sys
import json
import re

args = sys.argv

country_wiki ={}

with open(args[1]) as f:
    for l in f.readlines():
        country_wiki[json.loads(l)["title"]] = json.loads(l)["text"]

article_UK = country_wiki["イギリス"]


sections = []
for i in re.findall(r'(==+)(.*?)==+', article_UK):
    sections.append(''.join(i[1]+" "+str(len(i[0])-1))) 

print(sections)