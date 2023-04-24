# 16. ファイルをN分割するPermalink
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

N = int(input("N = "))

my_file = open("popular-names.txt", "r").readlines()

#["%.2d" % i for i in range(101)]

count = 0
while len(my_file) > 0:
    try:
        batch = my_file[0:N]
    except:
        batch = my_file

    with open("sp%.2d" % count, 'w') as fp:
        for item in batch:
            fp.write(item)
    my_file = my_file[N:]
    count = count + 1
