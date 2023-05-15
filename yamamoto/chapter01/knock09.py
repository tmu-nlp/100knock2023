import random
sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = sentence.split()
for i in range(len(words)):
    if len(words[i]) > 4:
        word = words[i]
        first = word[0]
        last = word[len(word)-1]
        word = word[1:len(word)-1]
        listed_word = list(word)
        random.shuffle(listed_word)
        words[i] = first + ''.join(listed_word) + last

print(' '.join(words))