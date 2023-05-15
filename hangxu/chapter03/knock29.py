#knock20:「イギリス」に関する記事本文uk
import json
with open('jawiki-country.json', 'r', encoding='utf-8') as f:
      for line in f:
        line = json.loads(line)
        if line['title']== 'イギリス':
            uk= line['text']
            break

#knock25:
import re
# テンプレート
pattern = r'\{基礎情報(.*?)^.}'  # .*?:可能な限り短いマッチ
template = re.findall(pattern, uk, re.MULTILINE + re.DOTALL) #re.MULTILINE:マッチした文字列のリストを返す,   re.DOTALL:.が改行にもマッチします
# 辞書オブジェクト
pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n))' #|:or, .+?:可能な限り短いマッチ,少なくでも1文字, s:space, ?::マッチ
result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))

#knock29：
import requests

def get_url(text):
    url_file = text['国旗画像'].replace(' ', '_')  #Flag_of_the_United_Kingdom.svg
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'#MediaWiki APIを使用してURLを取得する(?)
    data = requests.get(url)  #get request
    return re.search(r'"url":"(.+?)"', data.text).group(1)  #group(1):パターン内の括弧をキャプチャする。 

print(get_url(result))
