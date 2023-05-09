with open("col1.txt") as col1, open("col2.txt") as col2, open("knock13.txt", "w") as f:
    l = 0
    for line1 in col1:
        line2 = col2.readline()
        print(line1.strip() + '\t' + line2.strip(), file = f)
        
'''
UNIXコマンド

paste col1.txt col2.txt > knock13.txt
'''