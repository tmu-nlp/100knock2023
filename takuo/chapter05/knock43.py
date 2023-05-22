import knock41
import os

with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    chunked = knock41.getChunksList_paragraph(parsed_file.readlines())
    for paragraph in chunked:
        for chunk in paragraph:
            if (chunk.dst == -1):
                continue
            poss_self = []
            poss_dst = []
            dst_idx = chunk.dst-1
            for morph in chunk.morphs:
                poss_self.append(morph.pos)
            for morph in paragraph[dst_idx].morphs:
                poss_dst.append(morph.pos)
            if (("名詞" in poss_self) and ("動詞" in poss_dst)):  # 条件を満たすとき
                print(
                    f"{chunk.surface_no_punct()}\t{paragraph[dst_idx].surface_no_punct()}")
