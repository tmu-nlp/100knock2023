
import pandas as pd
df = pd.read_table('popular-names.txt', header=None, usecols=[0]) #header:列の名前
print(df[0].unique())