s = "stressed"
s_reverse = ""
for i in range(len(s)-1, -1, -1):
    s_reverse = s_reverse + s[i]

print(s_reverse)