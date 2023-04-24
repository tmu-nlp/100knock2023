def n_gram(target,n):
    return [ target[idx:idx+n] for idx in range(len(target)-n+1)]

target='I am an NLPer'
a=target.split(' ')

n_gram(a,2)
n_gram(target,2)
