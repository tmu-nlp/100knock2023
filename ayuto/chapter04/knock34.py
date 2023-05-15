from knock30 import knock30
DListList = knock30()
V=[]
K=[]
f=0
for i in range(len(DListList)):
    for j in range(len(DListList[i])):
        if DListList[i][j]["pos"] == "名詞":
            K.append(DListList[i][j]["surface"])
            f+=1
        elif f>1:
            V.append(K)
            K=[]
            f=0
print(V)