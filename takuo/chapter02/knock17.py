with open("chapter02/popular-names.txt", "r") as pns:
    tabled = [line.split() for line in pns.readlines()]
    names = set()
    for line in tabled:
        names.add(line[0])
    print(len(names))

# 136
