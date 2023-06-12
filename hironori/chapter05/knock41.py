from knock40 import Morph

class Chunk():
    def __init__(self, a, b):
        self.morphs = a
        self.dst = b
        self.srcs = []

def k41():
    with open ('ai.ja.txt.parsed', encoding='utf-8') as f:
        ans = []
        chunks = []
        rel = []
        for l in f:
            if l.split()[0] == '*':
                if int(l.split()[2].strip('D')) != -1:
                    rel.append((int(l.split()[1]), int(l.split()[2].strip('D')))) # (係り受け元, 係り受け先)
                chunks.append(Chunk([], int(l.split()[2].strip('D'))))
                continue
            if l == 'EOS' or l == 'EOS\n':
                if chunks == []:
                    continue
                for r in rel:
                    chunks[r[1]].srcs.append(r[0])
                ans.append(chunks)
                chunks = []
                rel = []
                continue
            d = Morph(l.split('\t')[0], l.split('\t')[1].split(',')[6], l.split('\t')[1].split(',')[0], l.split('\t')[1].split(',')[1])
            chunks[-1].morphs.append(d)
        return ans

if __name__=="__main__":
    for sc in k41():
        for c in range(len(sc)):
            print(c, ': ', end='')
            for m in sc[c].morphs:
                print(m.surface, end='')
            print(' ', sc[c].dst, sc[c].srcs)