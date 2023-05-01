with open('popular-names.txt') as f:
    
    dic = {}
    for line in f:
        if line.split()[0] not in dic:
            dic[line.split()[0]] = 1
        else:
            dic[line.split()[0]] += 1

    sorted_dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)

    #print(sorted_dic)
    for name in sorted_dic:
        print(name[0])