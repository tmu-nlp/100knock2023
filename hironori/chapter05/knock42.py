from knock40 import Morph
from knock41 import Chunk, k41

for sc in k41():
    for c in range(len(sc)):
        for m in sc[c].morphs:
            if m.surface == '、' or m.surface == '。':
                continue
            print(m.surface.strip('、。'), end='')
            if sc[c].dst != -1:
                print(end='\t')
                for md in sc[sc[c].dst].morphs:
                    print(md.surface.strip('、。'), end='')
            print()