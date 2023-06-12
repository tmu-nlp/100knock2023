from Structs import Morph, Chunk
import re
import os


def splitByParagraph(morphed_line_list: list) -> list:
    paragraphed = []
    buff = []
    for line in morphed_line_list:
        if (line == "EOS\n"):
            if (buff == []):
                continue
            else:
                paragraphed.append(buff)
                buff = []
        else:
            buff.append(line)
    return paragraphed


def genMorphs(mecabed_lines: list) -> list:
    morphs = []
    for line in mecabed_lines:
        m = Morph()
        m.build(line.rstrip('\n'))
        morphs.append(m)
    return morphs


def getChunksList_paragraph(morphed_line_list: list) -> list:
    # EOSでスプリットして，段落ごとに分ける．
    splted = splitByParagraph(morphed_line_list)

    # 頭から読んでいき，chunkのヘッダならChunk生成．
    # Chunk生成したら，行をピークし，ヘッダで無ければMorphを生成，Chunkの子とする
    # 全部のChunkの子を充実させたら，Chunksを頭から舐め，srcsを生成．
    # Chunk[i]のdstを見て，Chunks[self.dst].append(i+1)
    # そのあと文に分ける

    union = []
    for parag in splted:
        chunks_enum = []
        buff_line = []
        idx = 0
        # 子を充実させる
        while idx < len(parag):
            if (re.match(r"\* .*", parag[idx]) != None):  # if its header
                tmp_chunk = Chunk()
                tmp_chunk.build(parag[idx])
                # while peek is not header
                while (idx+1 < len(parag) and re.match(r"\* .*", parag[idx+1]) == None):
                    idx += 1
                    buff_line.append(parag[idx])
                tmp_chunk.morphs = genMorphs(buff_line)
                buff_line = []
                chunks_enum.append(tmp_chunk)
            else:
                idx += 1
        # srcsを生成
        for i in range(len(chunks_enum)):
            tar_id = chunks_enum[i].dst
            chunks_enum[tar_id].add_src(i+1)

        # 段落を文書全体に追加

        union.append(chunks_enum)
    return union


def getChunksList_centence(morphed_line_list: list) -> list:
    chunks_enum_paragraph = getChunksList_paragraph(morphed_line_list)
    chunks_list_centence = []

    for chunks_enum in chunks_enum_paragraph:
        centences = []
        buff_chunk = []
        for chunk in chunks_enum:  # 文を区切る
            if (chunk.morphs[-1].surface == '。'):
                buff_chunk.append(chunk)
                centences.append(buff_chunk)
                buff_chunk = []
            else:
                buff_chunk.append(chunk)
        if (centences == []):
            centences.append(buff_chunk)
        # 段落を文書全体に追加

        chunks_list_centence.append(centences)
    return chunks_list_centence


if __name__ == "__main__":
    with open(f"{os.path.dirname(__file__)}/ai.ja.txt.parsed", "r") as parsed_file:
        chunked = getChunksList_centence(parsed_file.readlines())
        print(chunked[4])
