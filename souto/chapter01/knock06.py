def ngram(si, size):
    ans=set()
    gen=""
    for i in range(len(si)):
        if(not(si[i]==" "or si[i]=="," or si[i]==".")):
            gen=gen+si[i]
            if(len(gen)==size):
                ans.add(gen)
                gen=gen[1:]
    return ans


a="paraparaparadise"
b="paragraph"

c=ngram(a, 2)
c1=ngram(b, 2)
print(c|c1)
print(c&c1)
print(c-c1)
print("se" in c)
print("se" in c1)