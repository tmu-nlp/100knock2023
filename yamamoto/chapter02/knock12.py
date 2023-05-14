import pandas as pd

popular_names = pd.read_table("https://nlp100.github.io/data/popular-names.txt", header=None)
popular_names.iloc[:,0].to_csv('col1.txt', header=None, index=None)
popular_names.iloc[:,1].to_csv('col2.txt', header=None, index=None)
