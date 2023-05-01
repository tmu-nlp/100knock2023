
file_path = 'popular-names.txt'


data = open(file_path, 'r', encoding='UTF-8')
data = ''.join(data)
data = data.replace('\t',' ')
data = data.splitlines()
# data = ['Mary F 7065 1880', 'Anna F 2604 1880', ...]
n_data = []


for row in data:
    buffer_list = row.split(' ')
    n_data.append(buffer_list[0])

n_data = set(n_data)

print (len(n_data))