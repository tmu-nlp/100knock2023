#出力する辞書のリスト
result = []
#一文のリスト
sentence = []

with open('neko.txt.mecab', encoding="utf-8") as f:
    for line in f:
        if line != 'EOS\n':
            left = line.split('\t')
            right = left[1].split(',')
            sentence.append({'surface': left[0], 'base': right[6], 'pos': right[0], 'pos1': right[1]})
            if right[1] == '句点':
                result.append(sentence)
                sentence = []
#ここまでknock30の内容

import collections
list = []
for s in result:
    for morpheme in s:
        list.append(morpheme["surface"])

collections.Counter(list)

print(dict)