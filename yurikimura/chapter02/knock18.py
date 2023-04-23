# 18. 各行を3コラム目の数値の降順にソートPermalink
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

data = []

with open("popular-names.txt", "r") as my_file:
    for line in my_file:
        line = line.strip()
        word = line.split("\t")
        data.append(word)

data = sorted(data, key=lambda x: int(x[2]), reverse=True)

for item in data:
    print(f"{item[0]}	{item[1]}	{item[2]}	{item[3]}")
