s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
v = s.split(' ')
d = {}
for i in range(len(v)):
    v[i] = v[i].rstrip(',.')
    if i == 0 or (4 <= i and i <= 8) or i == 14 or i == 15 or i == 18:
        d[v[i][0]] = i+1
    else:
        d[v[i][1]] = i+1
print(d)