def cipher(s):
    a = ""
    for i in range(len(s)):
        if s[i].islower():
            a += str(219 - ord(s[i]))
        else:
            a += s[i]
    return a

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(cipher(s))