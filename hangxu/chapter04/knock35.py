import knock30
from knock30 import result

words = []  
for word in result:
    for a in word:
        words.append(a['surface'])


from collections import Counter
print(Counter(words))

