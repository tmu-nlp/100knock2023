# 23. セクション構造Permalink
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import re
from knock21 import get_article, show_index

def find_section(content):
    content_list = content.split('\n')
    for line in content_list:
        line.strip()
        pattern = r'^.*(\=\=.*\=\=.*).*$'
        if re.search(pattern, line):
            match = re.findall('=', line)
            print(line + "level :" + str(int(len(match)/2 - 1)))

if __name__ == "__main__":
    country = input("Country Name = ")
    articles = get_article('jawiki-country.json')

    if country == 'index':
        print(show_index(articles))

    else:
        for article in articles:
            if article['title'] == country:
                find_section(article['text'])
