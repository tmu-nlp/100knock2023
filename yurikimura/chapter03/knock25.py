'''
25. テンプレートの抽出Permalink
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
'''

import json
import re

def get_article(src_json):
    articles = []
    with open(src_json, "r") as my_file:
        for line in my_file:
            my_json = json.loads(line)
            articles.append(my_json)
    return articles

def find_basic_info(content):
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    info = re.findall(pattern, content, re.MULTILINE + re.DOTALL)

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, info[0], re.MULTILINE + re.DOTALL))
    return result

def show_index(articles):
    index = [article['title'] for article in articles]
    index.sort()
    return index

country = input("Country Name = ")
articles = get_article('jawiki-country.json')


if __name__ == "__main__":
    if country == 'index':
        print(show_index(articles))
    else:
        for article in articles:
            if article['title'] == country:
                print(find_basic_info(article['text']))
