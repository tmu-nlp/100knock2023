from knock40 import Morph
from knock41 import Chunk, k41

for sc in k41():
    for c in range(len(sc)):
        if any(m.pos == '動詞' for m in sc[c].morphs):
            ch = {}
            for m in sc[c].morphs:
                if m.pos == '動詞':
                    print(m.base, end='\t')
                    break
            for cn in sc[c].srcs:
                if any(m.pos == '助詞' for m in sc[cn].morphs):
                    s = []
                    k = ''
                    for md in sc[cn].morphs:
                        s.append(md.surface.strip('、。'))
                        if md.pos == '助詞' and k == '':
                            k = md.base
                    ch[''.join(s)] = k
                    srt = sorted(ch.items(), key=lambda x: x[1])
            print(' '.join(k[1] for k in srt), '\t', ' '.join(k[0] for k in srt))