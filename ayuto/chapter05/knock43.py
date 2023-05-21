import knock41
import re

chunk_list = knock41.read_text_chunk()
code_regex = re.compile(r"[。、「」（）『』〈〉]")

def pos_map(B):
    return B.pos

for i in range(len(chunk_list)):
    L2 = [[list(map(knock41.surface_map ,o.morphs)), o.dst, o.srcs] for o in chunk_list[i]]
    L1 = [[o.morphs, o.dst, o.srcs] for o in chunk_list[i]]
    D = dict()
    for j in range(len(L1)):
        moto = []
        saki = []
        for k in range(len(L1[j])-2):
            moto += list(map(pos_map, L1[j][k]))
            saki += list(map(pos_map, L1[int(L1[j][1][0][:-1])][k]))
        if "名詞" in moto and "動詞" in saki:
            D[j] = int(L1[j][1][0][:-1])
    
    for d in D:
        print(code_regex.sub("", "".join(L2[d][0]))+ "\t" + code_regex.sub("", "".join(L2[D[d]][0])))
    print("")