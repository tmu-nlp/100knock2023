filepath = 'popular-names.txt'
f = open(filepath,'r')

N = int(input('N = ')) #整数

def start(lines, n):
    return n * int(len(lines) / N) + min(len(lines) % N, n) #ファイルの第一の数　min：残る行は一個ずつ前のファイルに配る

lines = f.readlines()
for n in range(N):
    with open('split' +str(n), 'w') as w:  #ファイルを作成する
        w.write(''.join(lines[start(lines, n): start(lines, n+1)]))

