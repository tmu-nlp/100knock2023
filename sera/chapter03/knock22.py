import re
import json

with open("./chapter03/jawiki-country.json", encoding="utf-8") as f:
    for line in f:
        line = json.loads(line) #json文字列を辞書に変換
        if line["title"] == "イギリス": #lineは辞書型
            uk_text = line["text"]
            break


pattern = r"\[\[Category:(.*)\]\]"
remove_pattern = r'\|.*'
for line in uk_text.split("\n"):
    result = re.match(pattern, line)
    if result is None:
        continue #正規表現に一致しない場合スキップ
    ans = re.sub(remove_pattern, '', result.group(1))
    #re.sub(正規表現のパターン, 置換後の文字列, 検索対象の文字列)
    #返り値は置換後の文字列
    print(ans)