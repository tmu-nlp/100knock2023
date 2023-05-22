import knock41
import os
from operator import itemgetter
from Structs import Chunk


def dig_tree(paragraph: list[Chunk], start: Chunk):
    print(start.surface_no_punct(), end="")  # 自分のsurfaceを出力
    if (start.dst != -1):  # 掘る
        print(' -> ', end="")
        dig_tree(paragraph, paragraph[start.dst])
    else:
        print()


with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    chunked = knock41.getChunksList_paragraph(parsed_file.readlines())
    with open(f"{os.path.dirname(__file__)}/k45_out.txt", "w") as outfile:

        for parag in chunked:

            # 名詞を含むChunkを探し，Surfaceを表示
            # かかり先のChunkに行き，Surfaceを表示
            # これをdsc==-1になるまで繰り返す．
            for chunk in parag:
                noun_flag = False
                for morph in chunk.morphs:
                    if (morph.pos == "名詞"):  # 名詞を含むChunkであることを認識
                        noun_flag = True
                        break

                if (noun_flag):  # 木をさかのぼる
                    dig_tree(parag, chunk)


# cat k45_out.txt | sort | uniq -c | sort -k 1n
# grep -P "^(行う|なる|与える)\t" k45_out.txt
