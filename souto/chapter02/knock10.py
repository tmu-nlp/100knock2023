f = open('./popular-names.txt', 'r')

data = f.read()
print(data.count('\n') + 1)

f.close()

#wc -l popular-names.txt