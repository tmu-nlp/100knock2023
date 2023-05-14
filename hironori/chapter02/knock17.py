with open('popular-names.txt') as f:
    col1 = [l.split()[0] for l in f.readlines()]
    for l in sorted(set(col1)):
        print(l)

'''
UNIXコマンド

cut -f 1 popular-names.txt | sort | uniq
'''