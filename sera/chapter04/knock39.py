import knock30
import collections
import matplotlib.pyplot as plt

result = knock30.read_mecab("./chapter04/neko.txt.mecab")

words = []
for sentence_list in result:
    for sentence in sentence_list:
        if sentence["pos"] != "記号":
            words.append(sentence["base"])

c = collections.Counter(words)
ans = c.values()

#ここからがknock39
ans = sorted(list(ans), reverse=True)
order = [i + 1 for i in range(len(ans))]

plt.rcParams["font.family"] = "Meiryo"
fig, ax = plt.subplots()
ax.scatter(order, ans)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("出現頻度順位")
ax.set_ylabel("出現頻度")
plt.show()
