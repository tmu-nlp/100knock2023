with open("chapter02/popular-names.txt", "r")as pns:
    rawstr = pns.read()
    rawstr = rawstr.replace('\t', ' ')
    print(rawstr)
