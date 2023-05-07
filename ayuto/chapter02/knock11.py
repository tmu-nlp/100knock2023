"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

with open("popular-names.txt", "r") as f:
    popular_names = f.read().replace("\t", " ")

# 確認
with open("popular-names-sed.txt") as f:
    popular_names_knock11 = f.read()
print(popular_names == popular_names_knock11)
