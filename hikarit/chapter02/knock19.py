file_path = 'popular-names.txt'

data =[]
f = open(file_path, 'r', encoding='UTF-8')
for line in f:
    elements = line.strip().split()
    data.append(elements)
# data = [['Mary', 'F', '7065', '1880'], ['Anna', 'F', '2604', '1880']...] 
name_counter ={}
for colum in data:
    if colum[0] in name_counter:
        name_counter[colum[0]] += 1
    else:
        name_counter[colum[0]] = 1

name_counter = sorted(name_counter.items(),key=lambda x:x[1],reverse=True)

print(name_counter)
