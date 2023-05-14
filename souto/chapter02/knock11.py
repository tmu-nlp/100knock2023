f = open('popular-names.txt', 'r')

data = f.read()

print(data.replace('\t', ' '))

f.close()


#expand -t 1 popular-names.txt
