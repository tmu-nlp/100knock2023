st1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
useless_sign = [',', '.']

for i in range(len(useless_sign)):
    st1 = st1.replace(useless_sign[i],'')


words_list = st1.split(' ')
num_of_char_list = []





for i in range(len(words_list)):
    num_of_char_list.append(len(words_list[i]))
print(num_of_char_list)