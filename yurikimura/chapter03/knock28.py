'''
28. MediaWikiマークアップの除去Permalink
27の処理に加えて，テンプレートの値から
MediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
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

def remove_markup(text):
    pattern = r'\'{2,5}'
    text = re.sub(pattern, '', text)

    pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    text = re.sub(pattern, r'\1', text)

    # htmlタグの削除
    pattern = r'<.+?>'
    text = re.sub(pattern, '', text)
    # テンプレートの削除
    pattern = r'\**\{\{.*?\}\}'
    text = re.sub(pattern, '', text)
    # 外部リンク削除
    pattern = r'\[.*?\]'
    text = re.sub(pattern, '', text)
    return text

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
                result = find_basic_info(article['text'])
                removed = {k: remove_markup(v) for k, v in result.items()}
                print(removed)
