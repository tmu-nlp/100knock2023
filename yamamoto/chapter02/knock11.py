import pandas as pd

popular_names = pd.read_table("https://nlp100.github.io/data/popular-names.txt", header=None)
popular_names.to_csv('11.txt', sep=' ', header=None, index=None)
#  expand 11.txt