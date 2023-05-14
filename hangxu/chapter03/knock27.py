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

for a, b in result3.items():
    print(a + ' ' + re.sub(pattern2,'', b))