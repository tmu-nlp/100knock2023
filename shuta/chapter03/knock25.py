#25
#jsonファイルの読み込み(#20)
import pandas as pd
import json

json_jawiki = open('jawiki-country.json', 'r')
df_jawiki = pd.read_json(json_jawiki, lines= True)
jawiki_uk = df_jawiki.at[235, 'text'] #.atで列名・行名を指定し、単独の要素を抽出
print(jawiki_uk)

#本題
import re
field_name = re.findall('\|(.+)\s=\s', jawiki_uk) #フィールド名を取得
field_value = re.findall('\|.+\s=\s(.+)', jawiki_uk) #フィールド名に対応する値を取得
field_dict = {}

for i in range(len(field_name)):
  field_dict[field_name[i]] = field_value[i]

print(field_dict)