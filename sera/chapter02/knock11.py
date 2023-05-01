with open('popular-names.txt') as f:
    with open('11.txt', mode = 'w') as f2:
        for line in f:
            new_line = line.replace('\t', ' ')
            f2.write(new_line)