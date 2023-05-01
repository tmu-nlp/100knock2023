import re
f = open('popular-names.txt', 'r')

data = f.read()

f.close()

l = re.split('\t|\n', data)

l=[(l[4*i], l[4*i+1], int(l[4*i+2]), l[4*i+3]) for i in range(int(len(l)/4))]
l.sort(key = lambda x: x[2], reverse=True)
l=[l[i][0] + '\t' + l[i][1] + '\t' + str(l[i][2]) + '\t' + l[i][3] for i in range(len(l))]
l='\n'.join(l)
print(l)