import re
import io
import sys
from knock40 import Morph

#入力を標準入力で読む wsl環境じゃないと動かない
with open("ai.ja.txt.parsed", "r") as f:
    _INPUT = f.read()
sys.stdin = io.StringIO(_INPUT)

class Chunk:
    """
    文節を受け取ってobjectを返すクラス
    """
    def __init__(self):
        self.morphs = []
        self.dst = [] # 係先
        self.srcs = [] # 係元
    def readChunk(self, clause) -> object:
        """
        文節のリストclauseを受け取りobjectを返す
        """
        #print("clause", clause)
        _, srcs_seed, dst_seed, _, _, _ = re.split(r"[\s/]", clause[0])
        self.dst.append(dst_seed) # 1文節には係先と係元1つしかないくない?
        self.srcs.append(srcs_seed)
        for word in clause[1:]:
            # print("word", word)
            m = Morph()
            self.morphs.append(m.readMorph(word))
        return self

def read_text_chunk():
    all_setnence_list = []
    setnence_list = []
    last_read_line = ""
    clause = []
    while True:
        try:
            line = input()
        except:
            return all_setnence_list
        if last_read_line == "EOS" and line[0] == r"*":
            clause.append(line)
        elif line[0] == r"*":
            if clause != []:
                c = Chunk()
                setnence_list.append(c.readChunk(clause))
            clause = [line]
        elif line == "EOS":
            if clause != []:
                c = Chunk()
                setnence_list.append(c.readChunk(clause))
            if setnence_list != []:
                all_setnence_list.append(setnence_list)
                clause = []
            setnence_list = []
        else:
            clause.append(line)
        last_read_line = line

# 出力
def surface_map(B):
    return(B.surface)
if __name__ == "__main__":
    print([[list(map(surface_map ,o.morphs)), o.dst, o.srcs] for o in read_text_chunk()[2]])