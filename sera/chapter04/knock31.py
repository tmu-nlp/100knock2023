import knock30

result = knock30.read_mecab("./chapter04/neko.txt.mecab")
#print(result[:3])

verb_set = set()

for sentence_list in result:
    for sentence in sentence_list:
        if sentence["pos"] == "動詞":
            verb_set.add(sentence["surface"])


print("動詞の種類:", len(verb_set))

for verb in list(verb_set)[:10]: #10個表示
    print(verb)