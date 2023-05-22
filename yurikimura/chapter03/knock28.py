'''
28. MediaWikiマークアップの除去Permalink
27の処理に加えて，テンプレートの値から
MediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
'''

import re
from knock21 import get_article, show_index
from knock25 import find_basic_info

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
