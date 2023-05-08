import re

f = open('col1.txt', 'r')
data = f.read()
f.close()

l = re.split('\n', data)
s=set(l)
s=list(s)

zerolist=[0 for i in range(len(s))]

d=dict(zip(s, zerolist))

for i in range(len(l)):
    d[l[i]]=d[l[i]]+1


l=list(d.items())
l.sort(key = lambda x: x[1], reverse=True)

l=[l[i][0]+' : '+str(l[i][1]) for i in range(len(l))]

print('\n'.join(l))


#cut -f 1 popular-names.txt | sort | uniq -c | sort -r