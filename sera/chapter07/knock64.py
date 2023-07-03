from gensim.models import KeyedVectors

GN_data = KeyedVectors.load_word2vec_format("./chapter07/GoogleNews-vectors-negative300.bin.gz", binary=True)


with open("./chapter07/questions-words.txt") as f1, open("./chapter07/knock64.txt", mode="w") as f2:
  for line in f1:
    line = line.split()
    if line[0] == ':':
      category = line[1]
    else:
      word, cos = GN_data.most_similar(positive=[line[1], line[2]], negative=[line[0]], topn=1)[0]
      f2.write(" ".join([category] + line + [word, str(cos) + "\n"]))