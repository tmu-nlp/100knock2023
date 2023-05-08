import pandas as pd

file_path = 'popular-names.txt'

#data = pd.read_table(file_path, sep = '\t')
data = open(file_path, 'r', encoding='UTF-8')
data = ''.join(data)
data = data.replace('\t',' ')

print (data)