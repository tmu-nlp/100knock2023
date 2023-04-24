def cipher(str1):
    list1 = list(str1)
    for i in range(len(list1)):
        if (list1[i].islower()):
            list1[i] = chr((219 - ord(list1[i])))
           
    return ''.join(list1)

msg = 'C:/Users/hikak/AppData/Local/Programs/Python/Python311/python.exe '
print(cipher(msg))