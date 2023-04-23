a=" Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

a=a.replace('.','')
a=a.replace(',','')

b=re.split(' ',a)
c=len(b)

i=0
while i<c:
    if i==0 or i==4 or i==5 or i==6 or i==7 or i==8 or i==14 or i==15 or i==18:
        x=b[i]
        print(x[0])
    else:
        y=b[i]
        print(y[0]+y[1])
    i+=1
