import pandas as pd

popular_names = pd.read_table("https://nlp100.github.io/data/popular-names.txt", header=None)

print(popular_names.iloc[:,0].value_counts())