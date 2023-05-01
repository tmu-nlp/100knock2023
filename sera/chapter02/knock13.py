with open('13.txt', mode = 'w') as f:
    f2 = open('col1.txt', mode = 'r')
    f3 = open('col2.txt', mode = 'r')

    col1_list = f2.readlines()
    col2_list = f3.readlines()
    
    for i in range(len(col1_list)):
        f.write(col1_list[i].replace('\n', '\t') + col2_list[i])