def n_gram(list, n):
    result = []
    for i in range(0, len(list)-n+1):
        result.append(list[i:i+n])
    return result

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)