from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'
path = './song/chapter04/neko.txt.mecab'
with open(path) as f:
    text = f.read().split('\n')
result = []
for line in text[:-1]:
    if line == 'EOS':
        continue
    ls = line.split('\t')
    d = {}
    tmp = ls[1].split(',')
    d = {'surface':ls[0], 'base':tmp[6], 'pos':tmp[0], 'pos1':tmp[1]}
    result.append(d)


surface =  [d['surface'] for d in result]
c = Counter(surface)
plt.hist(c.values(),  range = (1,10))
plt.savefig('./song/chapter04/fig38.png')