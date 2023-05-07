file_path = 'popular-names.txt'

data = open(file_path, 'r', encoding='UTF-8')
data = ''.join(data)
data = data.replace('\t',' ')

count_lines = data.count('\n')

print (count_lines)