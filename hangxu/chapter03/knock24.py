#knock20:「イギリス」に関する記事本文uk

import json
with open('jawiki-country.json', 'r', encoding='utf-8') as f:
      for line in f:
        line = json.loads(line)
        if line['title']== 'イギリス':
            uk= line['text']
            break

#knock24:
#ファイル:Adolf_Seel_Innenhof_der_Alhambra.jpg|  or ファイル:UKpop.svg| ...
import re

pattern = r'\[ファイル:(.+?)\|'
result = '\n'.join(re.findall(pattern, uk))
print(result)

