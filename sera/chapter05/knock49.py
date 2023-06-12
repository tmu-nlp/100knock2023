class Morph:
    def __init__(self, morph):
        surface, others = morph.split("\t")
        others = others.split(",")
        self.surface = surface
        self.base = others[6]
        self.pos = others[0]
        self.pos1 = others[1]

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

with open("./chapter05/ai.ja.txt.parsed") as f:
    blocks = f.read().split("EOS\n")

sentence_chunk = []
chunk_list = []
morphs = []

for block in blocks:
    block = block.split("\n")
    if block[0] == "":
        continue
    for sentence in block:
        if sentence =="":
            continue

        #blockの先頭が*だと, その文は係り受けの内容
        elif sentence[0] == "*":
            if len(morphs) > 0:
                chunk_list.append(Chunk(morphs,dst))
            dep = sentence.split(" ")
            dst = dep[2][:-1]
            morphs = []
            continue

        morphs.append(Morph(sentence))

    chunk_list.append(Chunk(morphs, dst))

    #Chunkに対して係り元の文節を追加
    for idx, chunk in enumerate(chunk_list):
        if chunk.dst != "-1":
            chunk_list[int(chunk.dst)].srcs.append(idx)
    sentence_chunk.append(chunk_list)
    chunk_list = []
    morphs = []



from itertools import combinations

def get_path_to_root(now, sentence):
    # 文節番号nowから根までのパスを求める
    # 出力は文節番号のリスト
    chunk = sentence[now]
    path = []
    if int(chunk.dst) != -1:
        path.append(now)
        nxt = chunk.dst
        while int(nxt) != -1:
            path.append(int(nxt))
            nxt = sentence[int(nxt)].dst
    return path



sentence = sentence_chunk[2]
nouns = []
# 名詞を含むchunkを抽出
for i, chunk in enumerate(sentence):
    if "名詞" in [morph.pos for morph in chunk.morphs]:
        nouns.append(i)

# 名詞を含むchunkの全ペアを作成
for i, j in combinations(nouns, 2):
    pathx = get_path_to_root(i, sentence) # Xから根までのパス
    pathy = get_path_to_root(j, sentence) # Yから根までのパス
    path1 = []
    path2 = []
    path3 = []
    flg = 0
    if j in pathx:
        # パターン１
        for k in pathx:
            if k == i:
                morphs = "X" + "".join([m.surface if m.pos == "助詞" else "" for m in sentence[k].morphs])
                path1.append("".join(morphs))
            elif k != j:
                morphs = "".join([m.surface if m.pos != "記号" else "" for m in sentence[k].morphs])
                path1.append("".join(morphs))
            else:
                morphs = "Y" + "".join([m.surface if m.pos == "助詞" else "" for m in sentence[k].morphs])
                path1.append("".join(morphs))
                break
        print(" -> ".join(path1))
    else:
        # パターン2
        for k in pathx:
            if k == i:
                morphs = "X" + "".join([m.surface if m.pos == "助詞" else "" for m in sentence[k].morphs])
                path1.append("".join(morphs))
            elif k not in pathy:
                morphs = "".join([m.surface if m.pos != "記号" else "" for m in sentence[k].morphs])
                path1.append("".join(morphs))
            else:
                break
        for l in pathy:
            if l == j:
                morphs = "Y" + "".join([m.surface if m.pos == "助詞" else "" for m in sentence[l].morphs])
                path2.append("".join(morphs))
            elif l != k:
                morphs = "".join([m.surface if m.pos != "記号" else "" for m in sentence[l].morphs])
                path2.append("".join(morphs))
            elif l == k or flg:
                flg = 1
                morphs = "".join([m.surface if m.pos != "記号" else "" for m in sentence[l].morphs])
                path3.append("".join(morphs))

        print(" -> ".join(path1) + " | " + " -> ".join(path2) + " | " + " -> ".join(path3))

# https://mori-memo.hateblo.jp/entry/2022/09/04/172210 を参考にしました