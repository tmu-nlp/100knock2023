def n_gram(n,lis):
    list1 = []
    list2 = []
    for i in range(len(lis)-n+1):
        for j in range(n):
            list2.append(lis[i+j])
            
        list1.append(tuple(list2[0:n]))
       
        list2.clear()

    return list1

st1 = 'paraparaparadise'
st2 = 'paragraph'

X = set(n_gram(2,st1))
Y = set(n_gram(2,st2))

print(X|Y)
print(X&Y)
print(X-Y)

print(('s','e') in (X|Y))