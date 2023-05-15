'''
38. ヒストグラムPermalink
単語の出現頻度のヒストグラムを描け．ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
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

    values = [data[i][1] for i in range(len(data))]

    plt.figure(figsize=(9, 4))
    plt.hist(values, bins=100)
    plt.show()
