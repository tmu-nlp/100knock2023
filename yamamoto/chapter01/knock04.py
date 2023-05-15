sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
word = sentence.split()
one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}
for i in range(len(word)):
    if i+1 in one:
        dict[word[i][0]] = i+1
    else:
        dict[word[i][0:2]] = i+1
#テスト
test = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mi", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]
for i in test:
    print(dict[i])