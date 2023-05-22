import knock41
import os
from operator import itemgetter

with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
    chunked = knock41.getChunksList_paragraph(parsed_file.readlines())
    with open(f"{os.path.dirname(__file__)}/k45_out.txt", "w") as outfile:

        for parag in chunked:

            # 動詞を含むChunkをさがす
            # 見つけた動詞の基本形を後で使う
            # みつけた動詞を含むChunkのsrcsを確認する．
            # src Chunkのうち，助詞をもつChunkをさがす
            # 助詞を持つChunkの(助詞Morphの表層形，Chunkの表層形)をリストに保持，助詞Morphでソートして出力
            for chunk in parag:
                for morph in chunk.morphs:
                    if (morph.pos == "動詞"):  # 動詞を含むChunkであることを認識，左端の動詞の表層形を保持
                        verb_surface = morph.surface
                        particles = []

                        src_chunk_id = chunk.srcs
                        for id in src_chunk_id:
                            src_chunk = parag[id-1]  # src chunkについて
                            for src_morph in src_chunk.morphs:  # src_chunkのmorphsが助詞を含むか判定，含むならappend
                                if (src_morph.pos == "助詞"):
                                    particles.append(
                                        (src_morph.surface, src_chunk.surface()))

                        # if(particles!=[]): #かかる助詞が無い場合を飛ばす？

                        particles = sorted(
                            particles, key=itemgetter(1))  # 辞書順にソート
                        outstr = verb_surface+'\t'
                        for pair in particles:
                            outstr += pair[0]+' '
                        for pair in particles:
                            outstr += pair[1]+' '
                        outstr = outstr[:-1]
                        print(outstr)

# cat k45_out.txt | sort | uniq -c | sort -k 1n
# grep -P "^(行う|なる|与える)\t" k45_out.txt
