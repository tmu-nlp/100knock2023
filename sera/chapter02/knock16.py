n = int(input())

with open('popular-names.txt') as f:
    line_list = f.readlines()
    f2 = open('16.txt', mode = 'w')
    # len = n*q + r
    # r < nが 成り立つ
    q = int(len(line_list) / n) # q行ずつ区切る
    r = len(line_list) - n*q

    cnt = 0
    flag = 0
    r_cnt = 0
    for line in line_list:
        if flag == 0: # 余りの分だけ1行増やす
            if cnt >= q+1:
                cnt = 0
                f2.write('\n')
            f2.write(line)
            cnt += 1
            r_cnt += 1
        else:
            if cnt >= q:
                cnt = 0
                f2.write('\n')
            f2.write(line)
            cnt += 1

        if r_cnt >= r: # 余りを消化した後の処理
            flag = 1

    f2.close()