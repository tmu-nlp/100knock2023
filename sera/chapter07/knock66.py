from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr

GN_data = KeyedVectors.load_word2vec_format("./chapter07/GoogleNews-vectors-negative300.bin.gz", binary=True)

ws353 = []
with open("./chapter07/combined.csv") as f:
  next(f) # 一行目はラベルなので使わない
  for line in f:  # 1行ずつ読込み, 単語ベクトルと類似度を計算
    line = [s.strip(" ") for s in line.split(",")]
    line.append(GN_data.similarity(line[0], line[1]))
    ws353.append(line)


# スピアマン相関係数の計算
human = np.array(ws353).T[2]
w2v = np.array(ws353).T[3]
correlation, pvalue = spearmanr(human, w2v)

print("スピアマン相関係数: " + str(correlation))