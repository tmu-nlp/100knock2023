import sys
import json

args = sys.argv

country_wiki ={}

with open(args[1]) as f:
    for l in f.readlines():
        country_wiki[json.loads(l)["title"]] = json.loads(l)["text"]

#type(article_UK) : <class 'str'>
article_UK = country_wiki["イギリス"]

# カテゴリ名を含む行を格納するlistを宣言
category = []

#article_UKはstr型なのでreadlines()ではなくsplitlines()
for l in article_UK.splitlines():
    if "[Category:" in l :
        category.append(l)
        
for i in range(len(category)):
    print(category[i])