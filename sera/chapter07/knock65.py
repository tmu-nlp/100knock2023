from gensim.models import KeyedVectors

GN_data = KeyedVectors.load_word2vec_format("./chapter07/GoogleNews-vectors-negative300.bin.gz", binary=True)

with open("./chapter07/knock64.txt") as f:
  sem_cnt = 0
  sem_cor = 0
  syn_cnt = 0
  syn_cor = 0
  for line in f:
    line = line.split()
    if not line[0].startswith("gram"): # gramで始まるのが文法的アナロジー
      sem_cnt += 1
      if line[4] == line[5]:
        sem_cor += 1
    else:
      syn_cnt += 1
      if line[4] == line[5]:
        syn_cor += 1

print("意味的アナロジー正解率: " + str(sem_cor/sem_cnt))
print("文法的アナロジー正解率: " + str(syn_cor/syn_cnt))