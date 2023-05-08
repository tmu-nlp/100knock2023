#22
#jsonファイルの読み込み(#20)
import pandas as pd
import json

json_jawiki = open('jawiki-country.json', 'r')
df_jawiki = pd.read_json(json_jawiki, lines= True)
jawiki_uk = df_jawiki.at[235, 'text'] #.atで列名・行名を指定し、単独の要素を抽出
print(jawiki_uk)

#本題
import re
category = re.findall('.*Category:(.*)]]', jawiki_uk)
category_list = []

for i in range(len(category)):
  element = re.sub('\|\*', '', category[i])
  category_list.append(element)

print(category_list)