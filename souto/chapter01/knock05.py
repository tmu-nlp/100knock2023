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

def ngramtango(si, size):
    start=-1
    num=0
    kari=[]
    end=0
    ans=set()
    gen=""
    for i in range(len(si)):
        if(not(si[i]==" "or si[i]=="," or si[i]==".")):
            if(start==-1):
                start=end=i
            else:
                end=i
        else:
            kari.append(si[start:end+1])
            start=-1
            if(len(kari)==size):
                ans.add(' '.join(kari))
                kari=kari[1:]

        if(end==len(si)-1):
            kari.append(si[start:])
            if(len(kari)==size):
                ans.add(' '.join(kari))
                kari=kari[1:]
    return ans

a="I am an NLPer"
print(ngramtango(a, 2))
print(ngram(a, 2))