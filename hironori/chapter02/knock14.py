with open('popular-names.txt') as f:
    N = int(input())
    for i in range(N):
        l = f.readline()
        print(l.strip())
        
'''
UNIXコマンド

head -n 10 popular-names.txt

※"10"を変更することで任意の行数を出力できる
'''