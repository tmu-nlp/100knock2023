'''
39. Zipfの法則Permalink
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
'''

import os
import matplotlib.pyplot as plt
import japanize_matplotlib # pip install japanese-matplotlib
from knock30 import token_mapping
from knock35 import word_count, pick_value

if __name__ == "__main__":
    neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
    tokens = token_mapping(neko_mecab)
    data = word_count(tokens)
    data = sorted(data.items(), key=pick_value, reverse=True)

    key = [i for i in range(1, len(data) + 1)]
    values = [data[i][1] for i in range(len(data))]

    plt.scatter(key, values)

    ax = plt.gca()
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show()
