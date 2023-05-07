# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べるPermalink
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

from collections import Counter

names_str = ""

with open("popular-names.txt", "r") as my_file:
    for line in my_file:
        line = line.strip()
        word = line.split("\t")[0]
        names_str = names_str + word + " "

name_dict = Counter(names_str.split())
name_dict = sorted(name_dict.items(), key=lambda x:x[1], reverse=True)

for pair in name_dict:
    print(f"{pair[1]} {pair[0]}")
