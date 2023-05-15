#37 「猫」と共起頻度の高い上位10語
import collections
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語対応

words= [] 
neko_list2= []
for lis in neko_list:
  words.append(lis)
  if lis['surface'] == '。':
    neko_list2.append(words)
    words = []


co_words = []
for lis in neko_list2:
  for dic in lis:
    if dic['surface'] =='猫':
        for i in range(len(lis)):
          if lis[i]['surface'] != '猫': #猫と猫の共起パターンを除去
            co_words.append(lis[i]['surface'])


co = collections.Counter(co_words)
co_words10_list = co.most_common(10)
co_words = [co_words10_list[i][0] for i in range(len(co_words10_list))]
co_counts = [co_words10_list[i][1] for i in range(len(co_words10_list))]

plt.bar(co_words,co_counts)
plt.title('頻度上位10語 『我輩は猫である』')
plt.xlabel('出現単語')
plt.ylabel('出現回数(回)')
plt.show()