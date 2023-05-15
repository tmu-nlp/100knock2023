'''
04. 元素記号Permalink
“Hi He Lied Because Boron Could Not Oxidize Fluorine.
New Nations Might Also Sign Peace Security Clause.
Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

src = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can."

ignorelist = [".", ","]
dst = {}

for i in ignorelist:
    src = src.replace(i, "")

for i, v in enumerate(src.split()):
    if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        dst[v[0]] = i+1
    else:
        dst[v[0:2]] = i+1

print(dst)

# {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8,
# 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15,
# 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
