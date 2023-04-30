with open("chapter02/popular-names.txt", "r") as pns:
    lines = pns.readlines()

    req_n = int(input())
    l_count = len(lines)
    for i in range(l_count-req_n, l_count):  # [2780-n,2780-n+1,...,2780]
        print(lines[i].rstrip('\n'))
