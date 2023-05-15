# 11. タブをスペースに置換Permalink
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open('popular-names.txt', 'r') as f:
    for line in f:
        print(line.rstrip().replace('\t', ' '))
