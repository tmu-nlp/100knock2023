#10
import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し
len(popular_names)

# wcコマンド
# wc /Users/shuta/Desktop/popular-names.txt