import knock41
import re

chunk_list = knock41.read_text_chunk()
code_regex = re.compile(r"[。、「」（）『』〈〉]")

def pos_map(B):
    return B.pos

code_regex = re.compile(r"[。、「」（）『』〈〉]")
for i in range(len(chunk_list)):
    L2 = chunk_list[i]
    L1 = [[o.morphs, o.dst, o.srcs] for o in chunk_list[i]]
    D = dict()
    for j in range(len(L1)):
        D[j] = int(L1[j][1][0][:-1])
    
    for d in D:
        joshi_list = []
        dousi = None
        for morph in L2[d].morphs:
            if morph.pos == "動詞":
                dousi = morph.base
                break

        for morph in L2[D[d]].morphs:
            if morph.pos == "助詞":
                joshi_list.append(morph.surface)
        joshi_list.sort()

        kou = []
        for morph in L2[D[d]].morphs:
            kou.append(morph.surface)


        if dousi and joshi_list:
            print(dousi, end="\t")
            print(*joshi_list, end="\t")
            print(code_regex.sub("","".join(kou)))
