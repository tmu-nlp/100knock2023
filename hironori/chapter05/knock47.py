from knock40 import Morph
from knock41 import Chunk, k41

for sc in k41():
    flg = False
    for c in range(len(sc)):
        if any(m.pos == '動詞' for m in sc[c].morphs):
            ch = {}
            for m in range(len(sc[c].morphs)):
                if sc[c].morphs[m].pos == '動詞':
                    for cn in sc[c].srcs:
                        if any(sc[cn].morphs[mn].pos1 == 'サ変接続' and sc[cn].morphs[mn+1].base == 'を' for mn in range(len(sc[cn].morphs)-1)):
                            flg = True
                            for mn in range(len(sc[cn].morphs)-1):
                                if sc[cn].morphs[mn].pos1 == 'サ変接続' and sc[cn].morphs[mn+1].base == 'を':
                                    print(sc[cn].morphs[mn].base + sc[cn].morphs[mn+1].base + sc[c].morphs[m].base, end='\t')
                break
            if flg == False:
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
            flg = False