with open("chapter02/popular-names.txt", "r") as pns:
    tabled = [line.split() for line in pns.readlines()]
    name_count = {}  # 名前をkey，出現数をvalue
    for line in tabled:
        existed_val = name_count.setdefault(line[0], 0)
        name_count[line[0]] += 1
    tbl_sorted = sorted(name_count.items(),
                        key=lambda pair: pair[1], reverse=True)
    # dict.items()は(key,value)のタプルのリストを返すらしい．へー
    # sortedもソート対象の配列の要素を並べ替えるため，lambda式にはタプルが渡される．
    for pair in tbl_sorted:
        print(pair[0], pair[1])
