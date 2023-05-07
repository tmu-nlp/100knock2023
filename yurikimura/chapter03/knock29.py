'''
29. 国旗画像のURLを取得するPermalink
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
'''
import json
import re
import requests

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
                result_rm = {k: remove_markup(v) for k, v in result.items()}

                S = requests.Session()
                URL = "https://commons.wikimedia.org/w/api.php"
                PARAMS = {
                    "action": "query",
                    "format": "json",
                    "titles": "File:" + result_rm['国旗画像'],
                    "prop": "imageinfo",
                    "iiprop":"url"
                }
                R = S.get(url=URL, params=PARAMS)
                DATA = R.json()
                PAGES = DATA['query']['pages']
                for k, v in PAGES.items():
                    print (v['imageinfo'][0]['url'])
