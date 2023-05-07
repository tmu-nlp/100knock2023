import pandas as pd

popular_names = pd.read_table("https://nlp100.github.io/data/popular-names.txt", header=None)
col1 = pd.read_csv("col1.txt", header=None)
col2 = pd.read_csv("col2.txt", header=None)
col1_2 = pd.concat([col1, col2], axis=1)
col1_2.to_csv("13.txt", sep='\t', header=None, index=None)
# paste 13.txt