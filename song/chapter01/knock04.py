chemical_elements = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"

# split the string into words
words = chemical_elements.split()

# initialize an empty dictionary
chemical_symbols = {}

# indices of words to extract first letter from
first_letter_indices = [0, 4, 5, 6, 7, 8, 14, 15, 18]

# loop through the words and extract the appropriate letters
for i, word in enumerate(words):
    if i in first_letter_indices:
        chemical_symbols[word[0]] = word
    else:
        chemical_symbols[word[:2]] = word

# print the dictionary
print(chemical_symbols)