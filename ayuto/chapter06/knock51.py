import re
code_regex = re.compile(r"[()\.[]{},]")
S=[]
with open(r"train.txt", "r", encoding="utf-8") as f:
    while True:
        try:
            L= f.readline()
            L = list(L.split("\t")[1].split(" "))
            #print(L)
            for l in L:
                S.append(code_regex.sub("", l))
        except:
            break
with open("train.feature.txt", "w", encoding="utf-8") as f:
    f.write("\t".join(S))
