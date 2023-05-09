#26
#jsonファイルの読み込み(#20)
import pandas as pd
import json

json_jawiki = open('jawiki-country.json', 'r')
df_jawiki = pd.read_json(json_jawiki, lines= True)
jawiki_uk = df_jawiki.at[235, 'text'] #.atで列名・行名を指定し、単独の要素を抽出
print(jawiki_uk)

#フィールド名・値の取得(#25)
field_name = re.findall('\|(.+)\s=\s', jawiki_uk) #フィールド名を取得
field_value = re.findall('\|.+\s=\s(.+)', jawiki_uk) #フィールド名に対応する値を取得

#本題
import re
field_value_list26 = []

for i in range(len(field_value)):
  value = re.sub(r'\'{2,}', '', field_value[i])
  field_value_list26.append(value)
  
print(field_value_list26)