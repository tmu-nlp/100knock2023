import re
import json

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
    
for k, v in dic.items():
    print(k,v)