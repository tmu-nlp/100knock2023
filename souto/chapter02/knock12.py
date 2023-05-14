import re
f = open('popular-names.txt', 'r')

data = f.read()

f.close()

l = re.split('\t|\n', data)

l1=[l[4*(i)] for i in range(int(len(l)/4))]
l2=[l[4*(i)+1] for i in range(int(len(l)/4))]

l1='\n'.join(l1)
l2='\n'.join(l2)

f=open('col1.txt', 'w')
f.write(l1)
f.close()
f=open('col2.txt', 'w')
f.write(l2)
f.close()
#cut -f 1 popular-names.txt
#cut -f 2 popular-names.txt
#デフォルトで区切り文字がタブ

