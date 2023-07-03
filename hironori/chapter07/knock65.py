'''
sem_n = 0
sem_a = 0
syn_n = 0
syn_a = 0
with open('/content/drive/MyDrive/questions-words-ans.txt') as f:
  for l in tqdm(f):
    l = l.split(' ')
    if not l[0].startswith('gram'):
      sem_n += 1
      if l[4] == l[5]:
        sem_a += 1
    else:
      syn_n += 1
      if l[4] == l[5]:
        syn_a += 1

print(f'semantic analogy: {sem_a/sem_n:.3f}')
print(f'semantic analogy: {syn_a/syn_n:.3f}')
'''