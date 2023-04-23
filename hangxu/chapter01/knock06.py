def n_gram(target,n):
    return [ target[idx:idx+n] for idx in range(len(target)-n+1)]

target='paraparaparadise'
X=set(n_gram(target,2))
print(X)

target='paragraph'
Y=set(n_gram(target,2))
print(Y)

X|Y
X&Y
X-Y

'se' in X
'se' in Y
