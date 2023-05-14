def cipher(x):
    l=list(x)
    for i in range(len(x)):
        if x[i].islower():
            l[i]=chr(219-ord(x[i]))
    return ''.join(l)


x="abcdA"
print(cipher(x))