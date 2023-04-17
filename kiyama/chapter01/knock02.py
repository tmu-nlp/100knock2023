word = "パタトクカシーー"
trg = ""

for i in range(len(word)):
    if i % 2 == 0:
        trg += word[i]

print(trg)
