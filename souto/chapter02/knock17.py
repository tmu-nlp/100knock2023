import re

f = open('col1.txt', 'r')
data = f.read()
f.close()

l = re.split('\n', data)

s=set(l)

print(s)