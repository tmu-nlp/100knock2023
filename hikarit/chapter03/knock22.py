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


#\[\[Category:(.*?)(?:\|.*)?\]\]

# "[[Category"　と　"]]"　に囲まれた部分をキャプチャ

#(.*?): 任意の文字列を取得する

# (?:\|.*)?: | に続く任意の文字列を非キャプチャ

category = re.findall(r'\[\[Category:(.*?)(?:\|.*)?\]\]', article_UK)

for i in range(len(category)):
    print(category[i])