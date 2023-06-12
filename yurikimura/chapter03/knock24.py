'''
24. ファイル参照の抽出Permalink
記事から参照されているメディアファイルをすべて抜き出せ．
'''

import re
from knock21 import get_article, show_index

def find_medium(content):
    content_list = content.split('\n')
    for line in content_list:
        line.strip()
        pattern = r'^.*\[\[ファイル:(.*?)(?:\|.*).*$'
        if re.search(pattern, line):
            ans = re.findall(pattern, line, re.MULTILINE)
            ans = "\n".join(ans)
    return ans

if __name__ == "__main__":
    country = input("Country Name = ")
    articles = get_article('jawiki-country.json')
    if country == 'index':
        print(show_index(articles))
    else:
        for article in articles:
            if article['title'] == country:
                print(find_medium(article['text']))

# output
# Country Name = イギリス
# Wembley Stadium, illuminated.jpg
