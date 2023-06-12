import pandas as pd

df = pd.read_csv('./song/chapter02/popular-names.txt', delimiter='\t', header=None)
new = df[0].unique()
new.sort()
print (new)