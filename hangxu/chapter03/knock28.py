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

#knock26:
#強調マークアップ'''を除去する
pattern1 = r'\'{2,5}'
result1 = {a: re.sub(pattern1,'', b) for a, b in result.items()}

#knock27
#[[記事名]] → 記事名 (ファイル以外)
pattern2 = r'\[\[(?!ファイル)([^\|]*?)\]\]'
result2 = {a: re.sub(pattern2, r'\1', b) for a, b in result1.items()}  #'\1'：同一パターンの文字列を抽出する
#[[記事名#節名|表示文字]] or [[記事名|表示文字]] → 表示文字 
pattern3 = r'\[\[(?!ファイル)(?:[^\|]*)\|(.*?)\]\]'
result3 = {a: re.sub(pattern3, r'\1', b) for a, b in result2.items()}

#knock28
#ファイルを除去する [[ファイル:...]]
pattern4 = r'\[\[ファイル:(.*?)\]\]'
result4 = {a: re.sub(pattern4, '', b) for a, b in result3.items()} 

#外部リンクを除去する [http://...] or {{Cite web|url=https://...}}
pattern5 = r'\[http:(.*?)\]|\{\{Cite web(.*?)\}\}'
result5 = {a: re.sub(pattern5, '', b) for a, b in result4.items()} 

#labelを除去する <...>
pattern6 = r'<.*?>'
result6 = {a: re.sub(pattern6, '', b) for a, b in result5.items()} 

#{{...}}を除去する
pattern7 = r'\{\{.*?\}\}'
result7 = {a: re.sub(pattern7, '', b) for a, b in result6.items()} 

for a, b in result7.items():
    print(a + ' ' + b)