import knock41
import re

chunk_list = knock41.read_text_chunk()

def pos_map(B):
    return B.pos
def base_map(B):
    return B.base
def surface_map(B):
    return B.surface
def pos1_pos_map(B):
    return([B.pos1, B.pos])

code_regex = re.compile(r"[。、「」（）『』〈〉*]")
for i in range(len(chunk_list)):
    L2 = chunk_list[i]
    adjacency_list = [[] for _ in range(len(L2))]
    for j in range(len(L2)):
        adjacency_list[int(L2[j].dst[0][:-1])].append(j)
    for j in range(len(adjacency_list)):
        pos_list = list(map(pos_map, (L2[j].morphs)))
        surface_list = list(map(surface_map, (L2[j].morphs)))
        vurv = []
        vurv_ = []
        kakarimoto = []
        if ["サ変接続", "名詞"] in list(map(pos1_pos_map, L2[j-1].morphs)):
            if "を" in list(map(base_map, L2[j-1].morphs)):
                vurv_.append(L2[j-1])
        if "動詞" in pos_list:
            for k in range(len(pos_list)):
                if pos_list[k] == "動詞":
                    vurv.append(list(map(base_map, (L2[j].morphs)))[k])
                    break
            for k in range(len(adjacency_list[j])):
                s = adjacency_list[j][k]
                for l in range(len(list(map(base_map, L2[s].morphs)))):
                    if s!=j-1 and list(map(pos_map, L2[s].morphs))[l] == "助詞":
                        kakarimoto.append([list(map(surface_map, L2[s].morphs))[l], list(map(surface_map, L2[s].morphs))])
                        break
        kakarimoto = sorted(kakarimoto)
        if vurv_ and vurv and kakarimoto:
            print(code_regex.sub("", "".join(list(map(base_map, vurv_[-1].morphs)))), end="")
            print(vurv[0], end="\t")
            for k in kakarimoto:
                print(k[0], end="\t")

            for k in range(len(kakarimoto)):
                print(code_regex.sub("", "".join(kakarimoto[k][1])), end=" ")
            print("")