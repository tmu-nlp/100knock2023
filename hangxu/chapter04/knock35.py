import knock30
from knock30 import result

words = []  
for word in result:
    for a in word:
        words.append(a['base'])


from collections import Counter
print(Counter(words))

