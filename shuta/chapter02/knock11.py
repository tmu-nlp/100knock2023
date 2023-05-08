#11
import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

popular_names.replace('\t',' ')

#sedコマンド
# sed -e 's/\t/ /g' /Users/shuta/Desktop/popular-names.txt