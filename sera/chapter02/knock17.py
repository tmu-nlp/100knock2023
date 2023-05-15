with open('popular-names.txt') as f:
    col1_set = set()
    for line in f:
        col1_set.add(line.split()[0])

print(col1_set)
