import knock41
import graphviz
import os

with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    chunked = knock41.getChunksList_paragraph(parsed_file.readlines())
    parag = chunked[1]
    dot = graphviz.Digraph('intro')
    dot.attr('node', fontname='MS Gothic')
    for chunk in parag:
        if (chunk.dst == -1):
            continue
        dst_idx = chunk.dst-1
        dot.edge(f"{chunk.surface_no_punct()}",
                 f"{parag[dst_idx].surface_no_punct()}")

    
    dot.render(f"{os.path.dirname(__file__)}/out.png")
