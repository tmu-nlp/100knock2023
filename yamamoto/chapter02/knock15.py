import pandas as pd

popular_names = pd.read_table("https://nlp100.github.io/data/popular-names.txt", header=None)
N = int(input())
print(popular_names.iloc[len(popular_names)-N:,:])
# tail popular-names.txt