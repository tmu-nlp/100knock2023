with open("chapter02/popular-names.txt")as pns:
    lines = pns.readlines()  # huge memory needed
    print(len(lines))

#2780