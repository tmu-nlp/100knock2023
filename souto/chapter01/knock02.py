a="パトカー"
b="タクシー"
c=""
for i in range(len(a+b)):
    if(i%2==0):
        c=c+a[i//2]
    else:
        c=c+b[i//2]

print(c)