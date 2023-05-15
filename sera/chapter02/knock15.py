n = int(input())

with open('popular-names.txt') as f:
    line = f.readlines()
    for i in range(n):
        print(line[-i].replace('\n', ''))
    
