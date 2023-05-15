s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
v = s.split(' ')
a = []
for i in range(len(v)):
    v[i] = v[i].rstrip(',.')
    a.append(len(v[i]))
print(a)