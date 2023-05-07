
file_path = 'popular-names.txt'
col1_path = 'col1.txt'
col2_path = 'col2.txt'


data = open(file_path, 'r', encoding='UTF-8')
data = ''.join(data)
data = data.replace('\t',' ')
data = data.splitlines()
# data = ['Mary F 7065 1880', 'Anna F 2604 1880', ...]

n_data = open(col1_path,'w',encoding='UTF-8')
s_data = open(col2_path,'w',encoding='UTF-8')

for row in data:
    buffer_list = row.split(' ')
    n_data.write(buffer_list[0] + '\n')
    s_data.write(buffer_list[1] + '\n')

print ()