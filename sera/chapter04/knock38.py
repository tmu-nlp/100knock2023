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

plt.rcParams["font.family"] = "Meiryo"
fig, ax = plt.subplots()
ax.hist(ans, bins=100)
ax.set_xlabel("出現頻度")
ax.set_ylabel("単語の種類数")
plt.show()