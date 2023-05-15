# 13. col1.txtとcol2.txtをマージPermalink
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open('col1.txt', 'r') as rf1:
    col1 = rf1.readlines()
with open('col2.txt', 'r') as rf2:
    col2 = rf2.readlines()
with open('2cols.txt', 'w') as wf:
    for i in range(len(col1)):
        wf.write(col1[i].rstrip() + '\t' + col2[i])
