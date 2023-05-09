n = int(input())

with open('popular-names.txt') as f:
    cnt = 0
    for line in f:
        if cnt > n-1:
            break
        cnt += 1
        
        print(line.replace('\n', ''))
    
