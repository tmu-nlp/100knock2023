#35 単語の出現頻度
import collections

words = []
for lis in neko_list:
  words.append(lis['surface'])

c = collections.Counter(words)
print(c)