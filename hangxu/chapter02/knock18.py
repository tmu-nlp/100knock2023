filepath = 'popular-names.txt'
f = open(filepath,'r')

import pandas as pd

df = pd.read_csv(f, sep='\t', header=None) #sep:デリミタ
print(df.sort_values(2 ,ascending=False)) #降順:こうじゅん