import knock35
from knock35 import words

from collections import Counter
freq = Counter(words) 
f = list(zip(*freq.most_common(10)))  #f: (words),(frequency)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font='IPAGothic')  #日本語

x = f[0]  
y = f[1]  
plt.bar(x, y)
plt.show()
