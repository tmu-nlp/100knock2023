a="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19

num=1
mozi=True

dic={}

start=0
end=-1
for i in range(len(a)):
    if(a[i]==" "or a[i]=="," or a[i]=="."):
        if(start!=-2):
            if(num in [1,5,6,7,8,9,15,16,19]):
                dic[a[start]]=num
            else:
                dic[a[start:start+2]]=num
            start=-2
            num=num+1

    elif(start==-2):
        start=end=i
    
    else:
        end=end+1

print(dic)
