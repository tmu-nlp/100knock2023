with open('popular-names.txt') as f:
    ls = f.readlines()
    lines = [(l.split()[0], l.split()[1], int(l.split()[2]), l.split()[3]) for l in ls]
    lines.sort(key=lambda x: x[2], reverse=True)
    for l in lines:
        print('\t'.join(str(i) for i in l))

'''
UNIXコマンド

sort -n -r -k 3 popular-names.txt
'''