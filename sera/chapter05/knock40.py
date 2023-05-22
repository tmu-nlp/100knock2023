class Morph:
    def __init__(self, morph):
        surface, others = morph.split("\t")
        others = others.split(",")
        self.surface = surface
        self.base = others[6]
        self.pos = others[0]
        self.pos1 = others[1]
        
with open("./chapter05/ai.ja.txt.parsed") as f:
    blocks = f.read().split("EOS\n")


sentence_morphs = []
morphs = []
for block in blocks:
    block = block.split("\n")
    if block[0] == "":
        continue
    for letter in block:
        if letter == "" or letter[0] == "*":
            continue
        morphs.append(Morph(letter))
    sentence_morphs.append(morphs)
    morphs = []

    
for i in sentence_morphs[1]:
    print(vars(i))

#varsでクラス内で保持している情報を獲得