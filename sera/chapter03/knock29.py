import re
import json
import requests

with open("./chapter03/jawiki-country.json", encoding="utf-8") as f:
    for line in f:
        line = json.loads(line) #json文字列を辞書に変換
        if line["title"] == "イギリス": #lineは辞書型
            uk_text = line["text"]
            break


pattern = r"^\{\{基礎情報 国\n(.+?)$\n\}\}"
result = re.findall(pattern, uk_text, re.MULTILINE+re.S)
dic = dict(re.findall(r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=$))", result[0], re.MULTILINE+re.S))
for k, v in dic.items():
    dic[k] = re.sub(r"\'{2,5}", "", v)
    
for k,v in dic.items():
    dic[k] = re.sub(r"\[\[(?:[^|]*?\|)??([^|]*?)\]\]", r"\1", v)

for k,v in dic.items():
    #URLを削除
    v = re.sub(r'\[https?://.+\]', '', v)
    #HTMLタグを削除
    v = re.sub(r'<.*>(.+)<\/.+>', r'\1', v)
    v = re.sub(r'<.*>', '', v)
    #テンプレートの削除
    v = re.sub(r'\{\{.*?\}\}', '' ,v)   

    dic[k] = v


uk_flag = dic["国旗画像"]
uk_flag = uk_flag.replace(" ", "_")
print(uk_flag)
S = requests.Session()
URL = "https://www.mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop":"url",
    "titles": "File:"+uk_flag
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
print(DATA)
uk_flag_url = DATA["query"]["pages"]["-1"]["imageinfo"][0]["url"]
print(uk_flag_url)