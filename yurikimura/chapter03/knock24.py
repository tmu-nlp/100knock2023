# 23. セクション構造Permalink
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import json
import re

def get_article(src_json):
    articles = []
    with open(src_json, "r") as my_file:
        for line in my_file:
            my_json = json.loads(line)
            articles.append(my_json)
    return articles

def find_section(content):
    content_list = content.split('\n')
    for line in content_list:
        line.strip()
        pattern = r'^.*\[\[ファイル:(.*?)(?:\|.*).*$'
        if re.search(pattern, line):
            ans = re.findall(pattern, line, re.MULTILINE)
            ans = "\n".join(ans)
            print(ans)

def show_index(articles):
    index = [article['title'] for article in articles]
    index.sort()
    return index

country = input("Country Name = ")
articles = get_article('jawiki-country.json')

if country == 'index':
    print(show_index(articles))

else:
    for article in articles:
        if article['title'] == country:
            find_section(article['text'])
