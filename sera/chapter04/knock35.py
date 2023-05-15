import knock30
import collections

result = knock30.read_mecab("neko.txt.mecab")
#print(result[:2])


words = []
for sentence_list in result:
    for sentence in sentence_list:
        if sentence["pos"] != "記号":
           words.append(sentence["base"])

c = collections.Counter(words)
ans = c.most_common()

for word in ans[:10]: #10個表示
    print(word)
        
