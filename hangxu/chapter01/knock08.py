def cipher(x):
    a=""
    for y in x:
        if y.islower():
            a+=chr(219-ord(y))
        else:
            a+=y
    return a


print(cipher(b))
print(cipher(cipher(b))
