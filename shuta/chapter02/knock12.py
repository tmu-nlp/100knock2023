#12
import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

col1 = popular_names[0]
col1.to_csv('col1.txt',  header=False, index=False)

col2 = popular_names[1]
col2.to_csv('col2.txt',  header=False, index=False)

#cutコマンド
#cut -f 1 /Users/shuta/Desktop/popular-names.txt