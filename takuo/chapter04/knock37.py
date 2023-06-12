from knock30 import get_mecabed_list
from operator import itemgetter
from matplotlib import pyplot
import japanize_matplotlib

mecabed = get_mecabed_list("chapter04/neko.txt.mecab")

words_with_neko = {}
for line in mecabed:
    surfs=[]
    for dic in line:
        if (dic["pos"] == "記号"):
            continue
        surfs.append(dic["base"])
    if ('猫' not in surfs):
        continue  # ループの先頭に戻る
    for word in surfs:
        words_with_neko.setdefault(word, 0)
        words_with_neko[word] += 1

del words_with_neko['猫']
words_with_neko_sorted = sorted(words_with_neko.items(),
                                key=itemgetter(1), reverse=True)

words = [tup[0] for tup in words_with_neko_sorted[0:10]]
counts = [tup[1] for tup in words_with_neko_sorted[0:10]]

barplt = pyplot.bar(words, counts)
pyplot.bar_label(barplt, label_type="edge")
pyplot.savefig("chapter04/out_knock37_.png")
