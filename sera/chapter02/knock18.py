with open('popular-names.txt') as f:
    f2 = open('18.txt', mode = 'w')

    line_list = f.readlines()

    for i in range(len(line_list)):
        line_list[i] = line_list[i].split()
    #print(line_list)
    sorted_line = sorted(line_list, key=lambda x: int(x[2]), reverse=True)
    #print(sorted_line)
    for line in sorted_line:
        f2.write('\t'.join(line) + '\n')

    f2.close()