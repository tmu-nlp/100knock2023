from knock30 import knock30
DListList = knock30()
V=[]
for i in range(len(DListList)):
    for j in range(len(DListList[i])):
        #if DListList[i][j]["surface"] == "の" and DListList[i][j]["pos"] == "助詞" and DListList[i][j]["pos1"] == "連体化":
        if DListList[i][j]["surface"] == "の":
            try:
                if DListList[i][j-1]["pos"] == "名詞":
                    A = (DListList[i][j-1]["surface"])
                if DListList[i][j+1]["pos"] == "名詞":
                    B = (DListList[i][j+1]["surface"])
                V.append(tuple([A, B]))
            except:
                continue
print(V)