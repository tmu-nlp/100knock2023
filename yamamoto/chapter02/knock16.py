import pandas as pd

popular_names = pd.read_table("https://nlp100.github.io/data/popular-names.txt", header=None)
N = int(input())
num_col = len(popular_names) // N
for i in range(N):
    print(popular_names.iloc[i*num_col: (i+1) * num_col,:])
