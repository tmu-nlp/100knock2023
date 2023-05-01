import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

popular_names.sort_values(2, ascending= False)

#sortコマンド
# cut -f 3  /Users/shuta/Desktop/popular-names.txt | sort -n -r
