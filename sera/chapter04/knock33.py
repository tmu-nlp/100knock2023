import knock30

result = knock30.read_mecab("neko.txt.mecab")
#print(result[:2])

ans = set()
ans_text = []
flag = [0]*2

for sentence_list in result:
    for sentence in sentence_list:
        if sentence["pos"] == "名詞":
            if flag[0] == 1 and flag[1] == 1:
                ans_text.append(sentence["surface"])
                ans.add("".join(ans_text))
                flag[0] = flag[1] = 0
            else:
                flag[0] = 1
                ans_text.append(sentence["surface"])
            continue #初期化を回避
        elif sentence["surface"] == "の":
            flag[1] = 1
            ans_text.append(sentence["surface"])
            continue #初期化を回避
        
        #初期化
        ans_text = []
        flag[0] = flag[1] = 0


print("AのBの形の数:", len(ans))

for text in list(ans)[:10]: #10個表示
    print(text)
        
