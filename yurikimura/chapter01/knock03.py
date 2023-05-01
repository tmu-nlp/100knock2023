'''
03. 円周率Permalink
“Now I need a drink, alcoholic of course,
after the heavy lectures involving quantum mechanics.”
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
'''


src = "Now I need a drink, alcoholic of course,\
    after the heavy lectures involving quantum mechanics."

src_alpha = src.replace(",", "").replace(".", "")
words = {}
for i in src_alpha.split(" "):
    words[i] = len(i)

dst = [v for _, v in words.items()]

print(dst)

# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
