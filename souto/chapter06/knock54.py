import pydot
from IPython.display import Image,display_png
from graphviz import Digraph
import knock41

a, chunks=knock41.keitaiso_and_kakariuke()#bがchunk
edges=[]
for chunk in chunks[10]:
    index=chunk.dst
    if(index==-1):
        continue
    text=""
    for i in chunk.morphs:
        text+=i.surface

    c=chunks[10][index]
    text1=""
    for i in c.morphs:
        text1+=i.surface
    edges.append([text, text1])

n = pydot.Node('node')
n.fontname = 'IPAGothic'
g = pydot.graph_from_edges(edges, directed=True)
g.add_node(n)
g.write_png('./ans44.png')
display_png(Image('./ans44.png'))
