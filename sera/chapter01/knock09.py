import random

def f(s):
    list = s.split()
    new_list = []
    for word in list:
        if len(word) <= 4:
            new_list.append(word)
            continue
        tmp = []
        for i in range(len(word)):
            if i == 0 or i == len(word)-1:
                continue
            tmp.append(word[i])
        random.shuffle(tmp)
        new_list.append(word[0] + "".join(tmp) + word[-1])

    return " ".join(new_list)

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(f(s))

