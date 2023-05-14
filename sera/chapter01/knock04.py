s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s_list = s.split()
print(s_list)
s_dic = {}
for i in range(1, len(s_list)+1):
    if i in [1,5,6,7,8,9,15,16,19]:
        s_dic[s_list[i-1][0]] = i
    else:
        s_dic[s_list[i-1][0:2]] = i
print(s_dic)
