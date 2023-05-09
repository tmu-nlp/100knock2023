#knock20:「イギリス」に関する記事本文uk

import json
with open('jawiki-country.json', 'r', encoding='utf-8') as f:
      for line in f:
        line = json.loads(line)
        if line['title']== 'イギリス':
            uk= line['text']
            break

#knock23:
import re

#セクション名を抽出する
result = re.findall('={2,}(.+?)(={2,})', uk)  #r:rawstring,  ={2,}:=2回以上,　 .+?:．1回

result1 = [a + ' ' + str(len(b) - 1) for a, b in result]
print('\n'.join(result1))
