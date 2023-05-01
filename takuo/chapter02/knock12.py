with open("chapter02/popular-names.txt", "r") as pns:
    tabled = [line.split() for line in pns.readlines()]
    col1 = ""
    col2 = ""
    for line in tabled:
        col1 += line[0]+'\n'
        col2 += line[1]+'\n'
    with open("chapter02/col1.txt", 'w') as out:
        out.write(col1)
    with open("chapter02/col2.txt", 'w') as out:
        out.write(col2)
