from knock40 import Morph
from knock41 import Chunk, k41

for sc in k41():
    for c in sc:
        text = []
        if '名詞' in [s.pos for s in c.morphs] and int(c.dst) != -1:
            current_chunk = c
            text.append(''.join([m.surface for m in current_chunk.morphs if not m.pos == "記号"]))
            next_chunk = sc[int(current_chunk.dst)]
            while int(current_chunk.dst) != -1:
                text.append(''.join([m.surface for m in next_chunk.morphs]))
                current_chunk = next_chunk
                next_chunk = sc[int(next_chunk.dst)]
            print(*text, sep=' -> ')