'''
36. 頻度上位10語Permalink
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''

import os
import matplotlib.pyplot as plt
import japanize_matplotlib # pip install japanese-matplotlib
from knock30 import token_mapping
from knock35 import word_count, pick_value

neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
dst = token_mapping(neko_mecab)
data = word_count(dst)
data = sorted(data.items(), key=pick_value, reverse=True)

names = [data[i][0] for i in range(10)]
values = [data[i][1] for i in range(10)]

plt.figure(figsize=(9, 4))
plt.bar(range(10), values, tick_label=names)
plt.show()
