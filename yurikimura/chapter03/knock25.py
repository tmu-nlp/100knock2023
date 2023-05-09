'''
25. テンプレートの抽出Permalink
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
'''

import re
from knock21 import get_article, show_index

def find_basic_info(content):
    '''
    マークダウンテキストの中から順序無しリストのグループを全件抽出したい場合は
    オプション re.MULTILINE と re.DOTALL を指定
    '''
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    info = re.findall(pattern, content, re.MULTILINE + re.DOTALL)

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, info[0], re.MULTILINE + re.DOTALL))
    return result

country = input("Country Name = ")
articles = get_article('jawiki-country.json')

if __name__ == "__main__":
    if country == 'index':
        print(show_index(articles))
    else:
        for article in articles:
            if article['title'] == country:
                print(find_basic_info(article['text']))

# Country Name = イギリス
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国',
# '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ir
# eland}}<ref>英語以外での正式国名:<br />\n*{{lang|gd|An Rìoghachd ...
