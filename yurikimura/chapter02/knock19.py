# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べるPermalink
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

from collections import defaultdict

name_dict = defaultdict(lambda: 0)
cnt = 0

with open("popular-names.txt", "r") as my_file:
    for line in my_file:
        line = line.strip()
        cnt += 1
        word = line.split("\t")
        name = word[0]
        name_dict[word[0]] += 1

name_dict = sorted(name_dict.items(), key=lambda x: x[1], reverse=True)

for name in name_dict:
    print(f"   {name[1]} {name[0]}")
