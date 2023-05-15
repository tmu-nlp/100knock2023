'''
27. 内部リンクの除去Permalink
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ（参考: マークアップ早見表）．

**** みんなできないやつ 再考案件 ****
'''

import re
from knock21 import get_article, show_index
from knock25 import find_basic_info

def remove_markup(text):
    pattern = r'\'{2,5}'
    text = re.sub(pattern, '', text)

    pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    text = re.sub(pattern, r'\1', text)

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
