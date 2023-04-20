def ngram(s, n):
    r = set()
    for i in range(len(s) - n + 1):
        r.add(s[i:i + n])
    return r

x, y = "paraparaparadise", "paragraph"
X, Y = ngram(x, 2), ngram(y, 2)
print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合(X-Y):", X - Y)
print("差集合(Y-X):", Y - X)
print("Xに'se'は", end='')
if 'se' in X:
    print("含まれる")
else:
    print("含まれない")
print("Yに'se'は", end='')
if 'se' in Y:
    print("含まれる")
else:
    print("含まれない")