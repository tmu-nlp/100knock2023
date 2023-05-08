#19
import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

popular_names[0].value_counts()

#cut,uniq,sortコマンド
# cut -f 1  /Users/shuta/Desktop/popular-names.txt | sort | uniq -c | sort -n -r
