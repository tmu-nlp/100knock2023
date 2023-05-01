filepath = 'popular-names.txt'
f = open(filepath,'r')

for data in f:
    data = data.replace('\t',' ')
    print(data)

#\t:タブ　
