file_path = 'popular-names.txt'

data = open(file_path, 'r', encoding='UTF-8')
data = ''.join(data)
data = data.replace('\t',' ')
data = data.splitlines()
# data = ['Mary F 7065 1880', 'Anna F 2604 1880', ...]

N = input('type a number:')
N = int (N)

q, r = len(data) // N, len(data) % N

splited_data =[]

for i in range(r):
    splited_data.append(data[(q+1)*i: (q+1)*(i+1)])

for i in range(N-r):
    splited_data.append(data[(q+1)*r+q*i: (q+1)*r+q*(i+1)])



print (splited_data)