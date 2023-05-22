import MeCab

#neko.txt.mecabファイルを作成
-mecab ./neko.txt -o ./neko.txt.mecab
#headで確認
-head  ./neko.txt.mecab

#neko.txt.mecabについて
words_list =[]
neko_list = []
file = 'neko.txt.mecab'
with open("neko.txt.mecab") as f:
  for txt in f:
    lis = txt.split("\t")
    if len(lis) == 2:
        lis2 = lis[1].split(",")
        words_list.append({"surface": lis[0], "base": lis2[6], "pos": lis2[0], "pos1": lis2[1]})

# 不要な要素(空白や\u3000)が除去しきれていないので、words_listから除去する
for i in range(len(words_list)):
  if words_list[i]['surface'] != '\u3000' and words_list[i]['surface'] != '':
    neko_list.append(words_list[i])

#冒頭を表示
neko_list[0:10]