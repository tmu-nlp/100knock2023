# 14. 先頭からN行を出力Permalink
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

N = int(input("N = "))

with open('popular-names.txt', 'r') as f:
    for i in range(N):
        print(f.readline().rstrip())
