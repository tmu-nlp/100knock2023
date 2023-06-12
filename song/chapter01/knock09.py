import random
s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = []
text = s.split()
for word in text:
    if (len(word)>4):
        mid = list(word[1:-1])
        random.shuffle(mid)
        word = word[0] + ''.join(mid) + word[-1]
        ans.append(word)
    else:
        ans.append(word)
print (' '.join(ans))