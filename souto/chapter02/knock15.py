import sys
import re
num=int(sys.argv[1])

f = open('popular-names.txt', 'r')
data = f.read()
f.close()

l = re.split('\n', data)

l='\n'.join(l[len(l)-num:])

print(l)

#tail -n 10 popular-names.txt