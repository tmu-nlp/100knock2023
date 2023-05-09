a="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

li=[]

start=0
end=-1
for i in range(len(a)):
    if(a[i]==" "or a[i]=="," or a[i]=="."):
        if(start!=-2):
            li.append(end-start+1)
            start=-2
    
    elif(start==-2):
        start=end=i
    
    else:
        end=end+1

print(li)
    