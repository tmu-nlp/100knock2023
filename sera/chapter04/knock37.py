import knock30
import collections
import matplotlib.pyplot as plt

result = knock30.read_mecab("./chapter04/neko.txt.mecab")

words = []
for sentence_list in result:
    if "猫" in [sentence["surface"] for sentence in sentence_list]:
        for sentence in sentence_list:
            if sentence["pos"] != "記号" and sentence["pos"] != "助動詞"\
                and sentence["pos"] != "助詞" and sentence["surface"] != "猫":
                words.append(sentence["base"])


c = collections.Counter(words)
ans = c.most_common()

top10_words = [w[0] for w in ans[:10]]
top10_words_count = [w[1] for w in ans[:10]]

plt.rcParams["font.family"] = "Meiryo"
fig, ax = plt.subplots()
ax.bar(top10_words, top10_words_count)
ax.set_xlabel("頻出単語")
ax.set_ylabel("出現頻度")
plt.show()