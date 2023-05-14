index1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]

st1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

words_list = st1.split(' ')

dic_ele = {}

for i in range(len(words_list)):
    if i+1 in index1:
        dic_ele.setdefault(words_list[i][0],i+1)
    else:
        dic_ele.setdefault(words_list[i][0:2],i+1)


print(dic_ele)