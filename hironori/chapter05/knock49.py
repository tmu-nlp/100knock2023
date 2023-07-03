from knock40 import Morph
from knock41 import Chunk, k41

for sc in k41():
    for s in sc:
        pl, nl = [], [c for c in s if '名詞' in [m.pos for m in c.morphs]]
        for i in range(len(nl) - 1):
            st1 = [''.join([m.surface if m.pos != '名詞' else 'X' for m in nl[i].morphs])]
            for e in nl[i + 1:]:
                dst, p = nl[i].dst, []
                st2 = [''.join([m.surface if m.pos != '名詞' else 'Y' for m in e.morphs])]
                while int(dst) != -1 and dst != s.index(e):
                    p.append(s[int(dst)])
                    dst = s[int(dst)].dst
                if len(p) < 1 or p[-1].dst != -1:
                    mid = [''.join([m.surface for m in c.morphs if m.pos != '記号']) for c in p]
                    pl.append(st1 + mid + ['Y'])
                else:
                    mid, dst = [], e.dst
                    while not s[int(dst)] in p:
                        mid.append(''.join([m.surface for m in s[int(dst)].morphs if m.pos != '記号']))
                        dst = s[int(dst)].dst
                    ed = [''.join([m.surface for m in s[int(dst)].morphs if m.pos != '記号'])]
                    pl.append([st1, st2 + mid, ed])
    for p in pl:
        if isinstance(p[0], str):
            print(' -> '.join(p))
        else:
            print(p[0][0], ' -> '.join(p[1]), p[2][0], sep=' | ')