import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(df.iloc[:,0].value_counts())  #iloc[行，列]