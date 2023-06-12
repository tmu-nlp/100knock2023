import numpy as np
import matplotlib.pyplot as plt
import re
import knock30
import japanize_matplotlib


r=knock30.keitaiso()

start=0
flag=False
ans={}
for i in range(len(r)):
    if(r[i]!='EOF' and r[i]['surface']=='猫'):
        flag=True
    if(r[i]=='EOF'):
        if(flag):
            for j in range(start, i):
                if(r[j]['surface'] in ans and r[j]['surface']!='猫'):
                    ans[r[j]['surface']]=ans[r[j]['surface']]+1
                else:
                    ans[r[j]['surface']]=1
            start=i+1
            flag=False
        else:
            start=i+1

ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)

left=[]
height=[]

for i in range(10):
    left.append(ans[i][0])  
    height.append(ans[i][1])

plt.bar(left, height)
plt.show()
