
def generate_word_ngrams(sentence, n):
    # Split the sentence into words
    words = sentence.split()
    # Create empty list to store n-grams
    ngrams = []
    # Loop through the words and generate n-grams
    for i in range(len(words)-n+1):
        ngram = ' '.join(words[i:i+n])
        ngrams.append(ngram)
    return ngrams

sentence = "I am NLPer"
word_ngrams = generate_word_ngrams(sentence, 2) # generates word bigrams
print(word_ngrams)