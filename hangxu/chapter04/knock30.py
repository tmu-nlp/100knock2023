# #!/bin/bash
# mecab < neko.txt > neko.txt.mecab

result = []
sentence = []
 
with open('neko.txt.mecab', 'r', encoding='UTF-8') as f:
  for line in f:
    l1 = line.split('\t')
    if len(l1) == 2:
      l2 = l1[1].split(',')
      sentence.append({'surface': l1[0], 'base': l2[4], 'pos': l2[0], 'pos1': l2[1]})
      if l2[1] == '句点':
        result.append(sentence)
        sentence = []
 
result

