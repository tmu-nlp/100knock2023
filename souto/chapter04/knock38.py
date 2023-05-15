import knock35
import numpy as np
import matplotlib.pyplot as plt
import re
import japanize_matplotlib
r=knock35.num_of_tango()


ans=[]

for i in range(len(r)):
    ans.append(r[i][1])


plt.hist(ans, bins=100)
plt.xlabel('出現頻度')
plt.ylabel('単語の種類数')
plt.show()