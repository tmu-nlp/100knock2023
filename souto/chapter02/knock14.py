import sys
import re
num=int(sys.argv[1])

f = open('popular-names.txt', 'r')
data = f.read()
f.close()

l = re.split('\n', data)

l='\n'.join(l[:num])

print(l)

#head -n10 popular-names.txt
#10行指定している


