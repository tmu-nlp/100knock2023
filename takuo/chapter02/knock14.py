with open("chapter02/popular-names.txt", "r") as pns:
    lines = pns.readlines()

    req_n = int(input())
    for i in range(req_n):
        print(lines[i].rstrip('\n'))
