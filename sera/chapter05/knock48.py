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


for i in range(len(sentence_chunk)):
    for chunk in sentence_chunk[i]:
        pos_list = [m.pos for m in chunk.morphs]
        if "名詞" in pos_list:
            surface_list = [m.surface for m in chunk.morphs if m.pos != "記号"]
            path_list = ["".join(surface_list)]
            dst = int(chunk.dst)
            while dst != -1:
                surface_list = [m.surface for m in sentence_chunk[i][dst].morphs if m.pos != "記号"]
                path_list.append("".join(surface_list))
                dst = int(sentence_chunk[i][dst].dst)
            if len(path_list) > 1:
                print("->".join(path_list))