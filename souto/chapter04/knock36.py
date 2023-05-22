import numpy as np
import matplotlib.pyplot as plt
import re
import knock35
import japanize_matplotlib
r=knock35.num_of_tango()

left=[]
height=[]
pattern = r"^(?:{'surface': ')(.*?)(?:')"
print(re.search(pattern, r[7][0]).group(1))
for i in range(10):
    left.append(re.search(pattern, r[i][0]).group(1))
    
    height.append(r[i][1])

plt.bar(left, height)
plt.show()
