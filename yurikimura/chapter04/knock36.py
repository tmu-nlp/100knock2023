'''
36. 頻度上位10語Permalink
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''

import os
import matplotlib.pyplot as plt
import japanize_matplotlib # pip install japanese-matplotlib
from knock30 import token_mapping
from knock35 import word_count, pick_value

# def word_count(tokens):
#     counts = {}

#     for data in tokens:
#         if data["surface"] in counts.keys():
#             counts[data["surface"]] += 1
#         else:
#             counts[data["surface"]] = 1

#     return counts

# def pick_value(x):
#     return x[1]

if __name__ == "__main__":
    neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
    tokens = token_mapping(neko_mecab)
    data = word_count(tokens)
    data = sorted(data.items(), key=pick_value, reverse=True)

    names = [data[i][0] for i in range(10)]
    values = [data[i][1] for i in range(10)]

    plt.figure(figsize=(9, 4))
    plt.bar(range(10), values, tick_label=names)
    plt.show()
