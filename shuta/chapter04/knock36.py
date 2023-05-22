#36 頻度上位10語
import collections
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語対応

words10_list = c.most_common(10)

words = [words10_list[i][0] for i in range(len(words10_list))]
counts = [words10_list[i][1] for i in range(len(words10_list))]

plt.bar(words,counts)
plt.title('頻度上位10語 『我輩は猫である』')
plt.xlabel('出現単語')
plt.ylabel('出現回数(回)')
plt.show()