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



import graphviz

#Graphvizのオブジェクトを作成
g = graphviz.Graph(format="png", filename="dependency")
g.attr("node", fontname="IPAGothic")

n = 1
for chunk in sentence_chunk[n]:
    src_phrase_surface = [m.surface if m.pos != "記号" else "" for m in chunk.morphs]
    g.node("".join(src_phrase_surface))

for chunk in sentence_chunk[n]:
    src_phrase_surface = [m.surface if m.pos != "記号" else "" for m in chunk.morphs]
    dst_phrase_surface = [m.surface if m.pos != "記号" else "" for m in sentence_chunk[n][int(chunk.dst)].morphs]
    g.edge("".join(src_phrase_surface), "".join(dst_phrase_surface))

# 保存
g.view()