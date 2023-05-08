import random

def Typoglycemia(s):
    S = list(s.split())
    r = ""
    for i in S:
        if len(i) > 4:
            a = list(i[1:len(i)-1])
            random.shuffle(a)
            r += i[0] + ''.join(a) + i[-1]
        else:
            r += i
        if i != ".":
            r += " "
    return r

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(s))