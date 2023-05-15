def ngram(x):
  return [(x[i],x[i+1]) for i in range(len(x)-1)]

bigram1 = 'I am an NLPer'  #文字bi-gram用
bigram2 = bigram1.split()  #単語bi-gram用

print(ngram(bigram2)) #単語bi-gram
print(ngram(bigram1)) #文字bi-gram