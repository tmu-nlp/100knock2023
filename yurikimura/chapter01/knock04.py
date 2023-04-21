src = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

ignorelist = [".", ","]
dst = {}

for i in ignorelist:
    src = src.replace(i, "")

for i, v in enumerate(src.split()):
    if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        dst[v[0]] = i+1
    else:
        dst[v[0:2]] = i+1

print(dst)
