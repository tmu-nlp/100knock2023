'''
37. 「猫」と共起頻度の高い上位10語Permalink
「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''

import os
import matplotlib.pyplot as plt
import japanize_matplotlib
from knock30 import token_mapping

def cat_cooccur(tokens):
    counts = {}

    for i in range(len(tokens)):
        if tokens[i]["surface"] == "猫":

            if tokens[i+1]["pos"] != "記号":
                if tokens[i+1]["surface"] in counts.keys():
                    counts[tokens[i+1]["surface"]] += 1
                else:
                    counts[tokens[i+1]["surface"]] = 1

            if tokens[i-1]["pos"] != "記号":
                if tokens[i-1]["surface"] in counts.keys():
                    counts[tokens[i-1]["surface"]] += 1
                else:
                    counts[tokens[i-1]["surface"]] = 1

    return counts

if __name__ == "__main__":
    neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
    tokens = token_mapping(neko_mecab)
    data = cat_cooccur(tokens)

    data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    names = [data[i][0] for i in range(10)]
    values = [data[i][1] for i in range(10)]

    plt.figure(figsize=(9, 4))
    plt.bar(names, values)
    plt.show()
