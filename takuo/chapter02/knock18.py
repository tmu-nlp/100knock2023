with open("chapter02/popular-names.txt", "r") as pns:
    tabled = [line.split() for line in pns.readlines()]

    tabled.sort(key=lambda item: int(item[2]))
    # lambda式．sort()は通常先頭要素で比較する．ここでのlambda式の引数には['James', 'M', '87063', '1952']等の配列が入るので，3カラム目をkeyにして比較するようにしてやる．
    # operator.itemgetter()でもいいらしい．
    # intで比較しないと，文字コードでの比較となりNG

    print('\n'.join(['\t'.join(line) for line in tabled]))
