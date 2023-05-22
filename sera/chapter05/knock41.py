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
            #chunk_id, 係り先の番号, 主辞（文節の中心となる単語）/機能語（助詞など）の位置，　Score
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

for chunk in sentence_chunk[1]:
    print([m.surface for m in chunk.morphs], chunk.dst, chunk.srcs)