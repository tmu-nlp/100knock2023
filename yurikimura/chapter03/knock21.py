# 21. カテゴリ名を含む行を抽出Permalink
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re

with open("20.txt", "r") as data:
    for line in data:
        line = line.strip()
        pattern = r'^(.*\[\[Category:.*\]\]).*$'
        if re.search(pattern, line):
            print(line)
