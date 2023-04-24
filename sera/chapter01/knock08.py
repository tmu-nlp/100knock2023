def cipher(s):
    new_s = []
    for i in s:
        if 97 <= ord(i) <= 122:
            i = chr(219 - ord(i))
        new_s.append(i)
    return "".join(new_s)
s = "This is a pen"
new_s = cipher(s)
print(new_s)
print(cipher(new_s))