#14
import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

N = 5
popular_names.head(N)

#headコマンド
# head -n 5 /Users/shuta/Desktop/popular-names.txt