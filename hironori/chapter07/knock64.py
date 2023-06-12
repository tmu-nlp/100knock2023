'''
from tqdm import tqdm
with open('/content/drive/MyDrive/questions-words.txt') as f:
  ls = f.read().splitlines()

d = []
c = None
for l in tqdm(ls):
    if l.startswith(':'):
        c = l[2:]
    else:
        lst = [c] + l.split(' ') + list(model.most_similar(positive=[l.split(' ')[1], l.split(' ')[2]], negative=[l.split(' ')[0]], topn=1)[0])
        d.append(lst)

with open('/content/drive/MyDrive/questions-words-ans.txt', 'w') as fo:
  for i in d[:10]:
    fo.write(' '.join([str(j) for j in i]) + '\n')
'''