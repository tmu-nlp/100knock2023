class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

result = []
sentence = []
# Morphオブジェクトいれてく
with open('ai.ja.txt.parsed', encoding='utf-8') as f:
    for line in f:
        if line != 'EOS\n':
            if line[0] == '*':
                continue
            left = line.split('\t')[0]
            right = line.split('\t')[1].split(',')
            sentence.append(Morph(left, right[6], right[0], right[1]))
        else:
            result.append(sentence)
            sentence = []

if __name__ == "__main__":
    for i in result[2]:
        print(vars(i))