
col1_path = 'col1.txt'
col2_path = 'col2.txt'
marged_data_path = 'marged_data.txt'

n_data = open(col1_path,'r',encoding='UTF-8')
s_data = open(col2_path,'r',encoding='UTF-8')
marged_data = open(marged_data_path,'w',encoding='UTF-8')


n_data = ''.join(n_data)
n_data = n_data.split()

s_data = ''.join(s_data)
s_data = s_data.split()
# n_data = ['Mary', 'Anna', 'Emma', 'Elizabeth', ...]
# s_data = ['F', 'F', 'F', ...]



for i in range(len(n_data)):
    marged_data.write(n_data[i] + '\t' + s_data[i] + '\n')

