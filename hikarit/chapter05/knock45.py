import knock41


filename = 'knock45.txt'
with open(filename, mode='w') as f:
    sentences = knock41.sentences #sentencesというクラスのリストを持ってくる
    for sentence in sentences: 
        for chunk in sentence.chunks:
            for morph in chunk.morphs:
                if morph.pos == '動詞':
                    cases = [] #初期化
                    for src in chunk.srcs:
                        for m in sentence.chunks[src].morphs: #係りもとの形態素に関して
                            if m.pos == '助詞': #その形態素が助詞ならば
                                cases.append(m.surface) #cases(格s)に追加
                    if len(cases) != 0: #係りもとに助詞が存在するなら
                        cases = sorted(list(set(cases))) #重複を消す
                        line = morph.base + '\t' + ' '.join(cases) #動詞の後にタブ、助詞の間はスペース
                        f.write(line)
                        f.write('\n') #end = '\n'が　write()では使えない
                    break