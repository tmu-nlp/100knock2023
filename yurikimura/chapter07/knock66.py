'''
66. WordSimilarity-353での評価
The WordSimilarity-353 Test Collectionの評価データをダウンロードし，
単語ベクトルにより計算される類似度のランキングと，人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
'''

import numpy as np
from scipy.stats import spearmanr
from gensim.models import keyedvectors

model = keyedvectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)

ws353 = []
with open('combined.csv', 'r') as f:
  next(f)
  for line in f:  # 1行ずつ読込み、単語ベクトルと類似度を計算
    line = [s.strip() for s in line.split(',')]
    line.append(model.similarity(line[0], line[1]))
    ws353.append(line)

# 確認
for i in range(5):
  print(ws353[i])


# スピアマン相関係数の計算
human = np.array(ws353).T[2]
w2v = np.array(ws353).T[3]
correlation, pvalue = spearmanr(human, w2v)

print(f'スピアマン相関係数: {correlation:.3f}')
