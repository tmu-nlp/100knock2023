class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

#ここから
class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst    = dst
        self.srcs   = []

sentences = []
sentence = []
morphs  = []
dst = 0
# Morphオブジェクトいれてく
with open('ai.ja.txt.parsed', encoding='utf-8') as f:
    for line in f:
        if line != 'EOS\n':
            if line[0] == '*':
                if morphs != []:
                    sentence.append(Chunk(morphs, dst))
                    morphs = []
                dst = int(line.split()[2].replace("D", ""))
            else:
                left = line.split('\t')[0]
                right = line.split('\t')[1].split(',')
                morphs.append(Morph(left, right[6], right[0], right[1]))
        else:
            sentence.append(Chunk(morphs, dst))
            sentences.append(sentence)
            morphs = []
            sentence = []

    for sentence in sentences:
        for i, chunk in enumerate(sentence):
            if chunk.dst != -1:
                sentence[chunk.dst-1].srcs.append(i)

for chunk in sentences[2]:
    s = ""
    for morph in chunk.morphs:
        s = s + morph.surface
    print(s, chunk.dst)