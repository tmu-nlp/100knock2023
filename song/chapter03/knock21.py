import pandas as pd
import re
pattern = re.compile('Category')
wiki = pd.read_json('./song/chapter03/enwiki-country.json.gz', lines = True)
uk = wiki[wiki['title']=='United Kingdom'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        print (line)