#15
import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

N = 5
popular_names.tail(N)

#tailコマンド
# tail -n 5 /Users/shuta/Desktop/popular-names.txt