#38 ヒストグラム
import collections
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語対応

words_list = c.most_common()
words_counts = [words_list[i][1] for i in range(len(words_list))]

#出現回数1-50回のヒストグラム
plt.hist(words_counts, bins=50, range=(1,50))
plt.title('単語出現頻度 『我輩は猫である』')
plt.xlabel('出現頻度(回)')
plt.ylabel('種類数(個)')
plt.show()

#出現回数51-9000回のヒストグラム
plt.hist(words_counts, bins=50, range=(51,9000))
plt.title('単語出現頻度 『我輩は猫である』')
plt.xlabel('出現頻度(回)')
plt.ylabel('種類数(個)')
plt.show()