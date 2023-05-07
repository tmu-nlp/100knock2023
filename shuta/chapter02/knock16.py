#16
import pandas as pd
import numpy as np
popular_names = pd.read_table('https://nlp100.github.io/data/popular-names.txt', header=None) #ヘッダー無し

N = 5
step = len(popular_names)// N

for n in range(N) :
  popular_names_copy = popular_names[n*step:(n+1)*step].assign(group=n)
  popular_names_copy.to_csv(str(n)+'.txt')


#splitコマンド
# split -n 5 /Users/shuta/Desktop/popular-names.txt