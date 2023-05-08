with open('popular-names.txt') as f:
    N = int(input())
    ls = f.readlines()
    for l in ls[-N:]:
        print(l, end='')
        
'''
UNIXコマンド

tail -n 10 popular-names.txt

※"10"を変更することで任意の行数を出力できる
'''