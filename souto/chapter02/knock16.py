import sys
import re
N=int(sys.argv[1])

f = open('popular-names.txt', 'r')
data = f.read()
f.close()

l = re.split('\n', data)

num=int(len(l)/N)
nownum=0


while (nownum+num<len(l)):
    f=open(str(nownum)+'.txt', 'w')
    a='\n'.join(l[nownum:nownum+num])
    f.write(a)
    f.close()
    nownum=nownum+num

if(nownum<len(l)):
    f=open(str(nownum)+'.txt', 'w')
    a='\n'.join(l[nownum:])
    f.write(a)
    f.close()
    nownum=nownum+num

#split -l 500 popular-names.txt