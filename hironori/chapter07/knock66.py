'''
from scipy.stats import spearmanr

human = []
w2v = []
with open('/content/drive/MyDrive/combined.csv', encoding='utf-8') as f:
    next(f)
    for r in f:
        cols = r.rstrip().split(',')
        human.append(float(cols[2]))
        w2v.append(model.similarity(cols[0], cols[1]))

correlation, pvalue = spearmanr(human, w2v)

print('スピアマン相関係数: {}'.format(correlation))
'''