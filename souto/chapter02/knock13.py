import re

f=open('col1.txt', 'r')
data1 = f.read()
l1 = re.split('\n', data1)
f.close()
f=open('col2.txt', 'r')
data2 = f.read()
l2 = re.split('\n', data2)
f.close()

l=[]
for i in range(len(l1)):
    l.append(l1[i]+'\t')
    l.append(l2[i]+'\n')
l=''.join(l)
f=open('knock13.txt', 'w')
f.write(l)
f.close()

#paste  col1.txt col2.txt > 13.txt
