import knock30
import collections
import matplotlib.pyplot as plt

result = knock30.read_mecab("neko.txt.mecab")

words = []
for sentence_list in result:
    for sentence in sentence_list:
        if sentence["pos"] != "記号":
           words.append(sentence["base"])

c = collections.Counter(words)
ans = c.most_common()


#ここからがknock36
top10_words = [w[0] for w in ans[:10]]
top10_words_count = [w[1] for w in ans[:10]]

plt.rcParams["font.family"] = "Meiryo"
fig, ax = plt.subplots() #FigureとAxesを同時に生成
ax.bar(top10_words, top10_words_count)
ax.set_xlabel("頻出単語")
ax.set_ylabel("出現頻度")
plt.show()