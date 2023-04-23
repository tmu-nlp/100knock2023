def ngram(x):
  return [(x[i],x[i+1]) for i in range(len(x)-1)]

#set型によって集合を扱える / 同じ値は格納されない
X = set(ngram("paraparaparadise"))
Y = set(ngram("paragraph"))

print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)
print("Xにse:", {('s', 'e')} <= X)
print("Yにse:", {('s', 'e')} <= Y)