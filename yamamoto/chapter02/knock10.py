import pandas as pd

popular_names = pd.read_table("https://nlp100.github.io/data/popular-names.txt", header=None)

print(len(popular_names))

#wc popular-names.txt
# 2780 11120 55026 popular-names.txt