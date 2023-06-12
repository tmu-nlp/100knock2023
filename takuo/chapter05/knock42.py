import knock41
import os

with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    chunked = knock41.getChunksList_paragraph(parsed_file.readlines())

    for paragraph in chunked:
        for chunk in paragraph:
            if (chunk.dst == -1):
                continue
            dst_idx = chunk.dst-1
            print(
                f"{chunk.surface_no_punct()}\t{paragraph[dst_idx].surface_no_punct()}")
        print()
