# 17. １列目の文字列の異なりPermalink
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

from collections import defaultdict

name_dict = defaultdict(lambda: 0)

with open("popular-names.txt", "r") as my_file:
    for line in my_file:
        line = line.strip()
        word = line.split("\t")
        name = word[0]
        name_dict[word[0]] += 1

unique_names = list(name_dict.keys())
unique_names.sort()

for name in unique_names:
    print(name)
