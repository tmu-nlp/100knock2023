N = 3
import pandas as pd
df = pd.read_csv('./song/chapter02/popular-names.txt', delimiter='\t', header=None)
step = - (-len(df) // N)
for n in range(N):
    df_split = df.iloc[n*step:(n+1)*step]
    df_split.to_csv('popular-names'+str(n)+'.txt', sep='\t',header=False, index=False)
