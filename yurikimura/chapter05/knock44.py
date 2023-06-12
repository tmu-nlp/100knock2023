'''
44. 係り受け木の可視化Permalink
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，Graphviz等を用いるとよい．
'''
import os
from graphviz import Digraph
from utils import k41

filepath = os.path.join(os.path.dirname(__file__), "ai.ja.txt.parsed")
sentences = k41(filepath)

edges = []
for id, chunk in enumerate(sentences[2].chunks):
    if int(chunk.dst) != -1:
            modifier = ''.join([morph.surface if morph.pos != "記号" else "" \
                for morph in chunk.morphs] + ['{'+str(id)+'}']) # indexを追加
            modifiee = ''.join([morph.surface if morph.pos != "記号" else ""\
                for morph in sentences[2].chunks[int(chunk.dst)].morphs] + ['{'+str(chunk.dst)+'}'])
            edges.append([modifier,modifiee])

dg = Digraph(format="png")
for pair in edges:
    dg.edge(pair[0],pair[1])
dg.render(f"./output44")
