#23
#jsonファイルの読み込み(#20)
import pandas as pd
import json

json_jawiki = open('jawiki-country.json', 'r')
df_jawiki = pd.read_json(json_jawiki, lines= True)
jawiki_uk = df_jawiki.at[235, 'text'] #.atで列名・行名を指定し、単独の要素を抽出
print(jawiki_uk)

#本題
import re
section = re.findall('==.*==', jawiki_uk)

for i in range(len(section)):

 number = section[i].count('=')//2-1  #各セクションについて'='の数をカウント、2で割り1を引く
 section_name = section[i].strip(r'=+')  # =+でsectionリスト内の=を削除
 print(number,section_name)