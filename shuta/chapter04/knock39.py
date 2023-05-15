#39 Zipfの法則
#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
import collections
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語対応
import numpy as np


x=[]
for i in range(len(words_counts)):
  if words_counts[i] != words_counts[i-1]:
    rank = i+1
    x.append(rank)
  
  else:
    x.append(rank)

y = words_counts

plt.xscale('log')
plt.yscale('log')
plt.plot(x, y)
plt.title('単語出現頻度(両対数) 『我輩は猫である』')
plt.xlabel('出現頻度順位(位)')
plt.ylabel('出現頻度(回)')
plt.show()