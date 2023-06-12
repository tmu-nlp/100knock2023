'''
26. 強調マークアップの除去Permalink
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
'''

import re
from knock21 import get_article, show_index
from knock25 import find_basic_info

# def find_basic_info(content):
#     '''
#     マークダウンテキストの中から順序無しリストのグループを全件抽出したい場合は
#     オプション re.MULTILINE と re.DOTALL を指定
#     '''
#     pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
#     info = re.findall(pattern, content, re.MULTILINE + re.DOTALL)

#     pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
#     result = dict(re.findall(pattern, info[0], re.MULTILINE + re.DOTALL))
#     return result

def remove_markup(text):
    pattern = r'\'{2,5}' # 2〜5個の'
    text = re.sub(pattern, '', text)
    return text

country = input("Country Name = ")
articles = get_article('jawiki-country.json')


if __name__ == "__main__":
    if country == 'index':
        print(show_index(articles))
    else:
        for article in articles:
            if article['title'] == country:
                result = find_basic_info(article['text'])
                removed = {k: remove_markup(v) for k, v in result.items()}
                print(removed)

# Country Name = イギリス
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '公...
