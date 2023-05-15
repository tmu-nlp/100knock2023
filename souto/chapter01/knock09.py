x="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
import random
def shuf(x):
    l=[]
    start=-1
    end=0
    for i in range(len(x)):
        if(x[i] in [' ', '.', ',']):
            if(start!=-1):
                l.append(list(x[start:end+1]))
                start=-1
        
        else:
            if(start==-1):
                start=end=i
            else:
                end=end+1
    
    ansli=[]

    for i in range(len(l)):
        if(len(l[i])>4):
            kari=l[i][1:-1]
            random.shuffle(kari)
            ansli.append([l[i][0]]+kari+[l[i][-1]])
        else:
            ansli.append(l[i])
    
    ans=""
    
    for i in range(len(ansli)):
        ans=ans+''.join(ansli[i])+' '

    return ans+'.'


print(shuf(x))
