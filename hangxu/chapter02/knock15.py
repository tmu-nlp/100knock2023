filepath = 'popular-names.txt'
f = open(filepath,'r')

import pandas as pd
df = pd.read_table(f, header=None)

N = int(input('N = '))

print(df.tail(N))
