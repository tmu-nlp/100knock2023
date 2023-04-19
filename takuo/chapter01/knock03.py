STR="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

def rm_punct(raw_string):
    puncts={'.',',',':',';','!','?','-',"'",'"','(',')','{','}','[',']'}
    formatted=""
    for c in raw_string:
        if(c not in puncts):
            formatted+=c
    return formatted

words=STR.split(' ')
words_len=[]
for w in words:
    w=rm_punct(w)
    words_len.append(len(w))
    
print(words_len)
