def n_gram(n,lis):
    list1 = []
    list2 = []
    for i in range(len(lis)-n+1):
        for j in range(n):
            list2.append(lis[i+j])
            
        list1.append(list(list2[0:n]))
       
        list2.clear()

    return list1

str1 = 'I am an NLPer'
words_list = str1.split(' ')
#print(words_list)
list3 = n_gram(2,words_list)
print(list3)

print(n_gram(2,str1))