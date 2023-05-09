with open('popular-names.txt') as f:
    f2 = open('col1.txt', mode = 'w')
    f3 = open('col2.txt', mode = 'w')

    for line in f:
        f2.write(line.split()[0] + '\n')
        f3.write(line.split()[1] + '\n')

    f2.close()
    f3.close()