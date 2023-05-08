import sys
import json
import re

def remove(text):
    text = re.sub(r'\'{2,5}',"",text)
    text = re.sub(r'\[\[(?:[^|]*?\|)*?([^|#]*?)(?:#[^|]*)??\]\]', r'\1', text)

    return text


args = sys.argv

country_wiki ={}

with open(args[1]) as f:
    for l in f.readlines():
        country_wiki[json.loads(l)["title"]] = json.loads(l)["text"]

#type(article_UK) : <class 'str'>
article_UK = country_wiki["イギリス"]


#type(template) = <class 'list'>
#type(template[0]) = <class 'str'>
template = re.findall(r'{{基礎情報 国\n((?:[^{}]+|{{(?:[^{}]+|{{.*?}})*}})*)}}', article_UK, re.DOTALL)

template_dict = {}


for element in re.findall(r'\|(.+?) = (.+?)\n', template[0]):

    template_dict[element[0]] = remove(element[1])




f = open("UK27.txt","w")


for key, value in template_dict.items():
    print(key, value)
    f.write(key+" "+value+"\n")