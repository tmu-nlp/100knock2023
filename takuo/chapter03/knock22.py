import re

with open("chapter03/uk_text.txt", 'r') as uktxt:
    txt = uktxt.read()
    # "Category:" + カテゴリ名 + '|'or']'
    matched = re.findall(r'.*Category:([^\|\]]*)', txt)
    # -> "Category:" の後に続く，|か]以外の文字集合
    # ()で囲むと，囲んだ正規表現にマッチする(囲んだ部分の表現に合う文字列を返す)．
    for i in matched[1:]:
        print(i)
