import random

STR = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."


def shuffle_body(str):
    if (len(str) > 4):
        shuf = [str[0]]
        shuf.extend(random.sample(str[1:-1], len(str)-2))
        shuf.append(str[-1])
        return ''.join(shuf)
    else:
        return str


words = STR.split(' ')
words_shuffled = []
for w in words:
    words_shuffled.append(shuffle_body(w))

print(words_shuffled)
