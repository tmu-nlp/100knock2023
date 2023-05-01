with open("chapter02/popular-names.txt", "r") as pns:
    lines = pns.readlines()
    filenum = int(input())
    child_linenum = len(lines)//filenum  # N分割した時の行数
    # 完全に等分できればそれで良し．
    # 等分できなかったら最後のファイルに余り分を一緒に入れる
    # 「N行ごとに分割する」なら楽なんですが…(splitコマンドを使うということは，これが題意？)

    for child_idx in range(filenum):
        # pick_rangeの範囲を子ファイルに入れる
        pick_range = range(child_idx*child_linenum,
                           (child_idx+1)*child_linenum)
        if (child_idx == filenum-1):
            pick_range = range(child_idx*child_linenum, len(lines))

        buff = ""
        for i in pick_range:
            buff += lines[i]

        with open("chapter02/k16_out/k16_{}.txt".format(child_idx), 'w') as out:
            out.write(buff)
