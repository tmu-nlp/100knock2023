def ngram(s, n):
    r = []
    for i in range(len(s) - n + 1):
        r.append(s[i:i + n])
    return r

s = "I am an NLPer"
print(ngram(s, 2))
print(ngram(s.split(' '), 2))