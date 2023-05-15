with open("col1.txt", "w") as col1, open("col2.txt", "w") as col2, open("popular-names.txt") as f:
    for line in f:
        print(line.split()[0], file=col1)
        print(line.split()[1], file=col2)
        
'''
UNIXコマンド

cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt
'''