# 22. カテゴリ名の抽出Permalink
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

from knock21 import get_article, show_index

def find_category(content:str):
    categories = ""
    content_list = content.split('\n')
    for line in content_list:
        if line.startswith('[[Category:'):
            categories = categories + \
                line.replace('[[Category:','').replace(']]','') \
                    + ', '
    return categories[:-2]

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
