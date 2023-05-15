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

def show_index(articles):
    index = [article['title'] for article in articles]
    index.sort()
    return index

def find_category(content:str):
    content_list = content.split('\n')
    for line in content_list:
        if line.startswith('[[Category:'):
            print(line)
    return

if __name__ == "__main__":
    country = input("Country Name = ")
    articles = get_article('jawiki-country.json')

    if country == 'index':
        print(show_index(articles))

    else:
        try:
            for article in articles:
                if article['title'] == country:
                    find_category(article['text'])
        except TypeError:
            pass


# output:

# Country Name = アメリカ合衆国
# [[Category:アメリカ合衆国|*]]
# [[Category:海洋国家]]
# [[Category:G8加盟国]]
# [[Category:連邦制国家]]
# [[Category:共和国]]
