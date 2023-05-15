import knock30

result = knock30.read_mecab("neko.txt.mecab")
#print(result[:2])


ans = set()

for sentence_list in result:
    ans_text = []
    for sentence in sentence_list:
        if sentence["pos"] != "名詞":
            if len(ans_text) > 1:
                ans.add("".join(ans_text))
            ans_text = []
        else:
            ans_text.append(sentence["surface"])

    if len(ans_text) > 1:
        ans.add("".join(ans_text))


print("名詞の連接の数:", len(ans))

for text in list(ans)[:10]: #10個表示
    print(text)
        
