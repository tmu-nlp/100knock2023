import knock41
import re

#この辺のはクラス内に実装した方が良かったかも
def pos_map(B):
    return B.pos
def base_map(B):
    return B.base
def surface_map(B):
    return B.surface
def pos1_pos_map(B):
    return([B.pos1, B.pos])
# map で扱えるように関数にした

chunk_list = knock41.read_text_chunk()

code_regex = re.compile(r"[。、「」（）『』〈〉*]")
for i in range(len(chunk_list)):
    L2 = chunk_list[i] # 1文のリストを取得["文節1(Chunk)", "文節2(Chunk)", "文節3(Chunk)"]
    adjacency_list = [[] for _ in range(len(L2))] # 隣接リストを初期化
    for j in range(len(L2)):
        adjacency_list[int(L2[j].dst[0][:-1])].append(j) # adjancency_list[i] に 文節iに係っている文節の番号が入った 隣接リストを構成
    for j in range(len(adjacency_list)):
        pos_list = list(map(pos_map, (L2[j].morphs)))
        surface_list = list(map(surface_map, (L2[j].morphs)))
        vurv = []
        vurv_ = [] # 動詞に"を"で接続している語のリスト
        kakarimoto = []
        if ["サ変接続", "名詞"] in list(map(pos1_pos_map, L2[j-1].morphs)):
            if "を" in list(map(base_map, L2[j-1].morphs)):
                vurv_.append(L2[j-1]) 
        if "動詞" in pos_list:
            for k in range(len(pos_list)):
                if pos_list[k] == "動詞":
                    vurv.append(list(map(base_map, (L2[j].morphs)))[k])
                    break
            for k in range(len(adjacency_list[j])): # 係っている語から助詞を抽出
                s = adjacency_list[j][k]
                for l in range(len(list(map(base_map, L2[s].morphs)))):
                    if s!=j-1 and list(map(pos_map, L2[s].morphs))[l] == "助詞": # "を"を除いた助詞
                        kakarimoto.append([list(map(surface_map, L2[s].morphs))[l], list(map(surface_map, L2[s].morphs))])
                        break
        kakarimoto = sorted(kakarimoto) # 多次元配列のソートをする時、keyを指定しないとき最初の要素でソートされる
        if vurv_ and vurv and kakarimoto:
            print(code_regex.sub("", "".join(list(map(base_map, vurv_[-1].morphs)))), end="")
            print(vurv[0], end="\t")
            for k in kakarimoto:
                print(k[0], end="\t")

            for k in range(len(kakarimoto)):
                print(code_regex.sub("", "".join(kakarimoto[k][1])), end=" ")
            print("")