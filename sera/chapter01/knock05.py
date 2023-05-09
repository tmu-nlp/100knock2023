def n_gram(list, n):
    result = []
    for i in range(0, len(list)-n+1):
        result.append(list[i:i+n])
    return result

s = "I am an NLPer"
s_list = s.split()

print(n_gram(s, 2))
print(n_gram(s_list, 2))