import knock30
from knock30 import result

words = []  
for word in result:

    for numb in range(len(word)):
        words.append(word[numb]['base'])

    for a in word:
        words.append(a['surface'])



from collections import Counter
print(Counter(words))

