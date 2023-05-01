STR1 = "paraparaparadise"
STR2 = "paragraph"


def rm_punct(raw_string):
    # remove punctuation marks
    puncts = {'.', ',', ':', ';', '!', '?', '-',
              "'", '"', '(', ')', '{', '}', '[', ']', '\t', '\n'}
    formatted = ""
    for c in raw_string:
        if (c not in puncts):
            formatted += c
    return formatted


def get_bigram_set(words):
    bi_gram = {words[i]+words[i+1] for i in range(len(words)-1)}
    return bi_gram


X = get_bigram_set(STR1)
Y = get_bigram_set(STR2)
union = X | Y
intersection = X & Y
difference = X-Y

print(union)
print(intersection)
print(difference)
print("'se' in X:", "se" in X)
print("'se' in Y:", "se" in Y)
