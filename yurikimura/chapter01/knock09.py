# 09. TypoglycemiaPermalink
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that I could actually
# understand what I was reading : the phenomenal power of the human mind .”）
# を与え，その実行結果を確認せよ．

import random
text = 'I couldn’t believe that I could actually understand \
    what I was reading : the phenomenal power of the human mind .'


def Typoglycemia(src: str):
    src_words = src.split()
    dst_words = []

    for word in src_words:
        if len(word) <= 4:
            dst_words.append(word)
        else:
            first_letter = word[0]
            last_letter = word[-1]
            mid_letter = word[1:-1]
            shuffled_letter = ''.join(random.sample(mid_letter, len(mid_letter)))
            dst_words.append(first_letter + shuffled_letter + last_letter)

    return ' '.join(dst_words)


print(Typoglycemia(text))


# I cduonl’t bvleeie that I cuold actlulay utsaedrnnd
# what I was riaedng : the pemnaneohl pweor of the human mind .
