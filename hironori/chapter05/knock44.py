import pydot

from knock40 import Morph
from knock41 import Chunk, k41

p = []
s = k41()[1]
for c in s:
    if c.dst != -1:
        su = ''.join([m.surface for m in c.morphs if m.pos != '記号'])
        nsu = ''.join([m.surface for m in s[c.dst].morphs if m.pos != '記号'])
    p.append((su, nsu))

img = pydot.Dot()
img.set_node_defaults(fontname="MS Mincho")
for s, t in p:
    img.add_edge(pydot.Edge(s, t))
img.write_png('result44.png')