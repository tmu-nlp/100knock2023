from graphviz import Digraph
dg = Digraph(format='png')

import knock41
import re

chunk_list = knock41.read_text_chunk()[1]
code_regex = re.compile(r"[。、「」（）『』〈〉]")
for i in range(1):
    L1 = [[list(map(knock41.surface_map ,o.morphs)), o.dst, o.srcs] for o in chunk_list]
    D = dict()
    for j in range(len(L1)):
        dg.node(code_regex.sub("", "".join(L1[j][0])))
        D[j] = int(L1[j][1][0][:-1])
    for d in D:
        dg.edge(code_regex.sub("", "".join(L1[d][0])), code_regex.sub("", "".join(L1[D[d]][0])))
dg.render('./dgraph', view=True)