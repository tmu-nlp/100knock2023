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

v_set = set()
noun = False
no = False
np = ""
for s in result:
    for i in range(len(s) - 2):
        if (s[i]["pos"] == "名詞") & (s[i+1]["surface"] == "の") & (s[i+2]["pos"] == "名詞"):
            v_set.add( s[i]["surface"] + "の" + s[i+2]["surface"] )

print(v_set)