with open('popular-names.txt') as f:
    col1 = [l.split()[0] for l in f.readlines()]
    d = {}
    for i in col1:
        d[i] = d.get(i, 0) + 1
    for n, c in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print(c, n)

'''
UNIXコマンド

cut -f 1 popular-names.txt | sort | uniq -c | sort -r
'''