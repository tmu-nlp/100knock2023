st1 = 'パタトクカシーー'
st2 = ''

num = len(st1) // 2

for i in range(num):
    st2 += st1[2*i + 1]

print(st2)