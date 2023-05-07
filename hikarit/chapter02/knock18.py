file_path = 'popular-names.txt'

data =[]
f = open(file_path, 'r', encoding='UTF-8')
for line in f:
    elements = line.strip().split()
    elements[2] = int(elements[2])
    data.append(elements)
# data = [['Mary', 'F', '7065', '1880'], ['Anna', 'F', '2604', '1880']...] 

sorted_data = sorted(data, key=lambda x: x[2],reverse= True)

for i in range(5):
    print (sorted_data[i], end='\n')