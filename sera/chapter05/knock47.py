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
        for morph in chunk.morphs:
            if morph.pos == "動詞":
                particle_list = []
                clause_list = []
                mining_result = ""
                for src in chunk.srcs:
                    if len(sentence_chunk[i][src].morphs) == 2 and\
                      sentence_chunk[i][src].morphs[0].pos == "名詞" and\
                      sentence_chunk[i][src].morphs[0].pos1 == "サ変接続" and\
                      sentence_chunk[i][src].morphs[1].surface == "を":
                      mining_result = sentence_chunk[i][src].morphs[0].surface + "を" + morph.base
                    else:
                        particle = [m.surface for m in sentence_chunk[i][src].morphs if m.pos == "助詞"]
                        if particle:
                            particle_list.append(particle[-1])
                            clause = "".join([m.surface for m in sentence_chunk[i][src].morphs])
                            clause_list.append((particle[-1], clause))
                if len(mining_result) != 0 and len(particle_list) > 0:
                    particle_list.sort()
                    clause_list.sort()
                    clause_output = " ".join([clause[1] for clause in clause_list])
        
                    output = mining_result + "\t" + " ".join(particle_list) + " " + clause_output
                    print(output)                        
                break