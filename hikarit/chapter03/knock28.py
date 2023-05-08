import sys
import json
import re

def remove(text):
    #''神よ女王を護り賜え'' -> 神よ女王を護り賜え
    text = re.sub(r'\'{2,5}',"",text)

    #<br /> -> null
    text = re.sub(r'<.+?>', '', text)

    #{{lang|fr|[[Dieu et mon droit]]}} -> [[Dieu et mon droit]]
    text = re.sub(r'\{\{lang\|[a-z]{2}\|(.*?)\}\}', r'\1', text)

    #{{仮リンク|リンゼイ・ホイル|en|Lindsay Hoyle}} -> リンゼイ・ホイル 
    text = re.sub(r'\{\{仮リンク\|(.*?)\|.*?\}\}', r'\1', text)

    #元首等肩書 [[イギリスの君主|女王]] -> 元首等肩書 女王　etc..
    text = re.sub(r'\[\[(?:[^|]*?\|)*?([^|]*?)\]\]', r'\1', text)
    
    text = re.sub(r'\[.+?\]', r'', text)

    #1801年{{0}}1月{{0}}1日 -> 1801年1月1日
    text = re.sub(r'\{\{.+?\}\}', r'', text)

    return text


"""
l~19 
r'\[\[(?:[^|]*?\|)*?([^|]*?)(?:#\]\]'

[[記事名]] -> 記事名
[[記事名|表示文字]] -> 表示文字
[[記事名#節名|表示文字]] -> 表示文字

(?:[^|]*?\|)*? 
|が現れるまでの文字列を0回以上繰り返し除外
([^|]*?)
|が現れるまでの文字列をキャプチャ [^|]は、|以外の任意の文字にマッチする


"""



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


""""

f = open("UK28.txt","w")


for key, value in template_dict.items():
    print(key, value)
    f.write(key+" "+value+"\n")
"""