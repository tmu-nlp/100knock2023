import gensim
from knock60 import model
import pandas as pd

df = pd.read_csv('/home/nevucide/wordsim353/combined.csv')
sim = []
for i in range(len(df)):
    line = df.iloc[i]
    sim.append(model.similarity(line['Word 1'],line['Word 2']))
df['w2v'] = sim 
df[['Human (mean)', 'w2v']].corr(method='spearman')