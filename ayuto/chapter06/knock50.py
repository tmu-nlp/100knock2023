import random
S=[]
with open(r"C:\Users\Ayuto\Downloads\NewsAggregatorDataset (1)\newsCorpora.csv", "r", encoding="utf-8") as f:
    while True:
        try:
            L= f.readline()
            L.split("\t")[3] in ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
            S.append(L)
        except:
            break
random.shuffle(S)
#print(S)
train = S[:int(len(S)*(0.8))]
valid = S[int(len(S)*(0.8)):int(len(S)*(0.9))]
test = S[int(len(S)*(0.9)):]
with open("train.txt", "w", encoding="utf-8") as f:
    f.write("".join(train))
with open("valid.txt", "w", encoding="utf-8") as f:
    f.write("".join(valid))
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("".join(test))