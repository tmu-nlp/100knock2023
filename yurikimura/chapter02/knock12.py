# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存Permalink
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

with open('popular-names.txt', 'r') as rf:
    with open('col1.txt', 'w') as wf1:
        with open('col2.txt', 'w') as wf2:
            for line in rf:
                elements = line.split('\t')
                wf1.write(elements[0] + '\n')
                wf2.write(elements[1] + '\n')
