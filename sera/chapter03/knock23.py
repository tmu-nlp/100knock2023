import re
import json

with open("./chapter03/jawiki-country.json", encoding="utf-8") as f:
    for line in f:
        line = json.loads(line) #json文字列を辞書に変換
        if line["title"] == "イギリス": #lineは辞書型
            uk_text = line["text"]
            break


pattern = r"^(==*)(.+)=+$"
for line in uk_text.split("\n"):
    result = re.match(pattern, line)
    if result is None:
        continue
    print(result.group(2).strip(' ='), len(result.group(1)))