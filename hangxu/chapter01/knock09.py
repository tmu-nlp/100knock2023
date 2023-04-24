a="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
a=a.replace(':','')
a=a.replace('.','')

import re
b = re.split(' ',a)

c=[]
for d in b:
    if len(d)>4:
        r=random.sample(d[1:len(d)-1],len(d)-2)
        c.append(d[0]+"".join(r)+d[len(d)-1])
    else:
        c.append(d)

print(c)
