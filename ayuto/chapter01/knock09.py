import random
S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
S = list(S.split())
for i in range(len(S)):
    if len(S[i]) > 4:
        l = list(S[i][1:-1])
        random.shuffle(l) #こんな標準ライブラリあるのか~
        S[i] = S[i][0] + "".join(l) + S[i][-1]
print(*S)