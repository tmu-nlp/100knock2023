file_path = 'popular-names.txt'


data = open(file_path, 'r', encoding='UTF-8')
data = ''.join(data)
data = data.replace('\t',' ')
data = data.splitlines()
# data = ['Mary F 7065 1880', 'Anna F 2604 1880', ...]

N = input('type a number:')
N = int (N)
for i in range(N):
    print(data[i])

print ()