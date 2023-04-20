STR = "I am an NLPer"


def rm_punct(raw_string):
    # remove punctuation marks
    puncts = {'.', ',', ':', ';', '!', '?', '-',
              "'", '"', '(', ')', '{', '}', '[', ']', '\t', '\n'}
    formatted = ""
    for c in raw_string:
        if (c not in puncts):
            formatted += c
    return formatted


def get_bigram(words):
    bi_gram = []
    for i in range(len(words)-1):
        bi_gram.append(words[i]+words[i+1])
    return bi_gram


words = [rm_punct(w) for w in STR.split(' ')]
# str_rm_punct = ''.join(words)
bigram_w = get_bigram(words)
bigram_c = get_bigram(STR)
print(bigram_w)
print(bigram_c)
