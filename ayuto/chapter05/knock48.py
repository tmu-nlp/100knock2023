import knock41
import re

chunk_list = knock41.read_text_chunk()

def pos_map(B):
    return B.pos
def base_map(B):
    return B.base
def surface_map(B):
    return B.surface

def saiki(A):
    if A != -1 and adjacency_list2[A] != []:
        print(code_regex.sub("", "".join(list(map(surface_map, L2[A].morphs)))), end=" -> ") #最後に矢印ついちゃうの直すのを面倒だったので妥協。ごめんなさい
        return saiki(adjacency_list2[A])
    else:
        return -1
# 再帰書くのヘタクソ

code_regex = re.compile(r"[。、「」（）『』〈〉*]")
for i in range(len(chunk_list)):
    L2 = chunk_list[i]
    #print(L2, "Aaaa")
    adjacency_list = [[] for _ in range(len(L2))]
    for j in range(len(L2)):
        adjacency_list[int(L2[j].dst[0][:-1])].append(j)
    
    adjacency_list2 = [None for _ in range(len(L2))]
    for j in range(len(adjacency_list)):
        for a in adjacency_list[j]:
            if a != j:
                adjacency_list2[a] = j
    #print(adjacency_list2)
    for j in range(len(adjacency_list2)):
        if "名詞" in list(map(pos_map, L2[j].morphs)):

            try:
                saiki(j)
            except:
                print("")
                continue
    