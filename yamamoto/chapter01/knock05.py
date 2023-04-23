def ngram(sentence, num):
    words = sentence.split()
    word_gram = []
    for i in range(len(words)-num+1):
        word_gram.append(words[i:i+num])
    sentence = sentence.replace(" ", "")
    char_gram = []
    for i in range(len(sentence)-num+1):
        char_gram.append(sentence[i:i+num])
    return word_gram, char_gram

sentence = "I am an NLPer"
word_gram = ngram(sentence, 2)[0]
char_gram = ngram(sentence, 2)[1]
for i in word_gram:
    print(i)
for i in char_gram:
    print(i)