#knock20:「イギリス」に関する記事本文uk
import json
with open('jawiki-country.json', 'r', encoding='utf-8') as f:
      for line in f:
        line = json.loads(line)
        if line['title']== 'イギリス':
            uk= line['text']
            break

#knock22:
import re
pattern1 = r'^(?:.*\[Category:(.*)]])$'  #?:categoryと]]が輸出しない
result = '\n'.join(re.findall(pattern1, uk, flags=re.MULTILINE)) 
print(result)