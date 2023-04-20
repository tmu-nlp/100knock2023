STR = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."


def rm_punct(raw_string):
    # remove punctuation marks
    puncts = {'.', ',', ':', ';', '!', '?', '-',
              "'", '"', '(', ')', '{', '}', '[', ']', '\t', '\n'}
    formatted = ""
    for c in raw_string:
        if (c not in puncts):
            formatted += c
    return formatted


words = [rm_punct(w) for w in STR.split(' ')]
words_len = [len(w) for w in words]

print(words_len)
