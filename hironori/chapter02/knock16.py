with open('popular-names.txt') as f:
    N = int(input())
    ls = f.readlines()
    row = len(ls) // N #分割後の行数
    a = len(ls) % N #余る行数
    now = 0 #どこまで書き込んだか
    for i in range(N):
        fo_name = f'knock16_{i}'
        with open(fo_name, 'w') as fo:
            for l in ls[now:now+row]:
                print(l, file=fo, end='')
            now = now+row
            if a > 0:
                print(ls[now], file=fo, end='')
                now += 1
                a -= 1

'''
UNIXコマンド

split -n l/10 -d popular-names.txt knock16_

※"10"を変更することで任意の分割数を選択できる
'''