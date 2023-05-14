import re

with open("chapter03/uk_text.txt", 'r') as uktxt:
    txt = uktxt.read()
    matched = re.findall(r'.*Category.*', txt)
    # matched[0] = {{Sisterlinks|commons=United Kingdom|commonscat=United Kingdom|s=Category:イギリス|n=Category:イギリス|voy=United Kingdom}} はcategory宣言ではない？
    for i in matched[1:]:
        print(i)
