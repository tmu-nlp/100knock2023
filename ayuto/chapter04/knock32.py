from knock30 import knock30
DListList = knock30()
V=[]
for DList in DListList:
    for D in DList:
        #print(D)
        if D["pos"] == "動詞":
            V.append(D["base"])
print(V)