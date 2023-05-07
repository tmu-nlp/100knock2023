# 05. n-gramPermalink
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．


def word_ngram(src: str, n: int):
    src_words = src.split()
    dst = [src_words[i:i+n] for i in range(len(src_words)-n+1)]
    return dst


def letter_ngram(src: str, n: int):
    dst = [src[i:i+n] for i in range(len(src)-n+1)]
    return(dst)


src = "I am an NLPer"

print(word_ngram(src, 2))
print(letter_ngram(src, 2))

# [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
