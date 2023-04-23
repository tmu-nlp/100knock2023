def ngram(sentence, num):
    char_gram = []
    for i in range(len(sentence)-num+1):
        char_gram.append(sentence[i:i+num])
    return char_gram

paradise = "paraparaparadise"
paragraph = "paragraph"

X_list = ngram(paradise, 2)
Y_list = ngram(paragraph, 2)
X = set()
Y = set()
for i in X_list:
    X.add(i)
for i in Y_list:
    Y.add(i)

XY_union = X | Y
XY_intersection = X & Y
XY_difference = X - Y

if 'se' in X:
    print("X")
if 'se' in Y:
    print("Y")