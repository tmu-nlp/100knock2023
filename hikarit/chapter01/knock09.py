import random

def typoglycemia(str1):
    list1 = str1.split(' ')
    for i in range(len(list1)):
        if len(list1[i]) > 4:
            list2 = list(list1[i])
            chare = list2.pop(len(list2)-1)
            chars = list2.pop(0)
            
            list2 =random.sample(list2,len(list2))
            list2.insert(0,chars)
            list2.insert(len(list2),chare)

            list1[i] = ''.join(list2)
    return ' '.join(list1)

            

ika = "I couldnt believe that I could actually understand what I was reading : the phenomenal power of the human mind"

print(typoglycemia(ika))