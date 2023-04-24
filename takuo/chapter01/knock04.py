STR = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ONE_HEAD_ID = [1, 5, 6, 7, 8, 9, 15, 16, 19]


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
dict = {}  # key:頭1or2文字 value:単語の位置
for i in range(len(words)):
    if (i+1 in ONE_HEAD_ID):  # 0-based -> 1-based
        dict[words[i][0]] = i+1
    else:
        dict[words[i][0:2]] = i+1
print(dict)
