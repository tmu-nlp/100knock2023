word_a = 'paraparaparadise'

word_b = 'pargrph'

split_a = list(word_a)
split_b = list(word_b)

bi_gram_a = []
bi_gram_b = []

for i in range(len(split_a)-1):
    bi_gram = "".join(split_a[i:i+2])
    bi_gram_a.append(bi_gram)
    print(bi_gram_a)

for i in range(len(split_b)-1):
    bi_gram = "".join(split_b[i:i+2])
    bi_gram_b.append(bi_gram)
    
set_a = set(bi_gram_a)
set_b = set(bi_gram_b)

uni_set = set_a.union(set_b)

inter_set = set_a.intersection(set_b)

diff_set = set_a.difference(set_b)

if 'se' in set_a:
    print('"se"is in set_a')
else:
    print('"se"is not in set_a')
    
if 'se' in set_b:
    print('"se"is in set_b')
else:
    print('"se"is not in set_b')    