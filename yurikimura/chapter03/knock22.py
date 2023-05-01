# 21. カテゴリ名を含む行を抽出Permalink
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import json

def get_article(src_json):
    articles = []
    with open(src_json, "r") as my_file:
        for line in my_file:
            my_json = json.loads(line)
            articles.append(my_json)
    return articles

def find_category(content:str):
    categories = ""
    content_list = content.split('\n')
    for line in content_list:
        if line.startswith('[[Category:'):
            categories = categories + \
                line.replace('[[Category:','').replace(']]','') \
                    + ', '
    return categories[:-2]

def show_index(articles):
    index = [article['title'] for article in articles]
    index.sort()
    return index

if __name__ == "__main__":
    country = input("Country Name = ")
    articles = get_article('jawiki-country.json')

    if country == 'index':
        print(show_index(articles))

    else:
        for article in articles:
            if article['title'] == country:
                print(find_category(article['text']))

## Output
# Country Name = 日本
# 日本|*, 島国, 現存する君主国, G8加盟国
