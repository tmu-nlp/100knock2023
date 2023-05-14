import re

with open("chapter03/uk_text.txt", 'r') as uktxt:
    txt = uktxt.read()
    # for line in lines:
    #     # ファイル:filename.hoge|~~~

    matched = re.findall(r'ファイル:([^\|\]]*)', txt)
    for i in matched:
        print(i)
