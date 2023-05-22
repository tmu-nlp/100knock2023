import knock35
import numpy as np
import matplotlib.pyplot as plt
import re
import japanize_matplotlib
import math

r=knock35.num_of_tango()
ansnum=[]
ansrank=[]

for i  in range(len(r)):
    ansrank.append(i+1)
    ansnum.append(r[i][1])

plt.scatter(ansrank, ansnum)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.show()