#13

#12の内容
import pandas as pd
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

col1 = popular_names[0]
col1.to_csv('col1.txt')

col2 = popular_names[1]
col2.to_csv('col2.txt')

#13の内容
merge = pd.concat([col1, col2], axis=1) #axis=1で、横方向の連結となる
merge.to_csv('merge.txt', sep='\t', header=False, index=False) #sep='\t'で、タブ区切りとなる

#pasteコマンド
# paste /Users/shuta/Desktop/col1.txt /Users/shuta/Desktop/col2.txt