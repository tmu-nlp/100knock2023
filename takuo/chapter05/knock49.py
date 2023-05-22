import knock41
import os
from operator import itemgetter
from Structs import Chunk
import itertools


def path_to_root(paragraph:list[Chunk],start:Chunk):
    chunk_list=[]
    chunk_list.append(start)
    node=paragraph[start.dst]
    while(node.dst!=-1):
        chunk_list.append(node)
        node=paragraph[node.dst]
    return chunk_list
def show_path(paragraph:list[Chunk],a:Chunk,b:Chunk): # show path a -> b
    a_to_root=path_to_root(paragraph,a)
    if(b in a_to_root):
        for node in a_to_root:
            



with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    chunked = knock41.getChunksList_paragraph(parsed_file.readlines())

    # 名詞句をリストにまとめる
    # combinations()で組み合わせを列挙
    # 各組み合わせに対して，show_path()

    for parag in chunked:
        noun_chunks = []  # 名詞句のリスト
        for chunk in parag:
            noun_flag = False
            for morph in chunk.morphs:
                if (morph.pos == "名詞"):  # 名詞を含むChunkであることを認識
                    noun_flag = True
                    break

            if (noun_flag):  # 木をさかのぼる
                noun_chunks.append(chunk)

        pairs = itertools.combinations(noun_chunks, 2)
        for pair in pairs:
            


# cat k45_out.txt | sort | uniq -c | sort -k 1n
# grep -P "^(行う|なる|与える)\t" k45_out.txt
