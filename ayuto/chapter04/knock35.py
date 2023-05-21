from knock30 import knock30
import collections
DListList = knock30()
V=[]
for DList in DListList:
    for D in DList:
        V.append(D["surface"])
c = collections.Counter(V)

print(c)