with open("knock11.txt", "w") as fo, open("popular-names.txt") as fi:
    for line in fi:
        print(line.replace('\t', ' '), file=fo, end='')
        
'''
UNIXコマンド

expand -t 1 popular-names.txt
'''