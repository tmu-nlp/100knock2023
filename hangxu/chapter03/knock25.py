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
for a, b in result.items(): #items:組み合わせ
  print(a + ' ' + b)

