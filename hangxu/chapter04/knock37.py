import knock30
from knock30 import result

neko = []
for a in result:
  if any(d["base"] == "猫" for d in a):
    for dic in a:
      neko.append(dic["surface"])

#count
from collections import Counter
n_freq = Counter(neko) 
f = list(zip(*n_freq.most_common(10)))

#plot
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font='IPAGothic')
x = f[0]  
y = f[1]  
plt.bar(x, y)
plt.show()
