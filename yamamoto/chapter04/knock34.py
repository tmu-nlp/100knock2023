#出力する辞書のリスト
result = []
#一文のリスト
sentence = []

with open('neko.txt.mecab') as f:
    for line in f:
        if line != 'EOS\n':
            left = line.split('\t')
            right = left[1].split(',')
            sentence.append({'surface': left[0], 'base': right[6], 'pos': right[0], 'pos1': right[1]})
            if right[1] == '句点':
                result.append(sentence)
                sentence = []
#ここまでknock30の内容

list = []
nouns = ""
for s in result:
    i = 0
    cnt = 1
    while i < len(s):
        if s[i]["pos"] == "名詞":
            nouns = s[i]["surface"]
            for j in range(i+1, len(s)):
                if s[j]["pos"] == "名詞":
                    nouns = nouns + s[j]["surface"]
                    cnt += 1
                else:
                    list.append(nouns)
                    break
        i += cnt

print(list)