filepath = 'popular-names.txt'
f = open(filepath,'r')

N = int(input('N = '))  #int:整数

for i in range(N):
    print(f.readline().strip())

