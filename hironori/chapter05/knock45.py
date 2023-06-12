from knock40 import Morph
from knock41 import Chunk, k41

for sc in k41():
    for c in range(len(sc)):
        if any(m.pos == '動詞' for m in sc[c].morphs):
            k = set()
            for m in sc[c].morphs:
                if m.pos == '動詞':
                    print(m.base, end='\t')
                    break
            for cn in sc[c].srcs:
                for md in sc[cn].morphs:
                    if md.pos == '助詞':
                        k.add(md.base)
            print(' '.join(sorted(k)))