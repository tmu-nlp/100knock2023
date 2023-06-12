'''
40. 係り受け解析結果の読み込み（形態素）Permalink
形態素を表すクラスMorphを実装せよ．このクラスは
表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，
各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
'''
from io import TextIOWrapper
import os

class Morph():
    def __init__(self, line:str):
        line = line.replace('\t', ',').split(',')
        self.surface = line[0]
        self.base = line[7]
        self.pos = line[1]
        self.pos1 = line[2]

    def make_json(self):
        return {"surface":self.surface, "base":self.base, "pos":self.pos, "pos1":self.pos1}

def load_file(fname:TextIOWrapper) -> list():
    EOS_list = fname.read().split("EOS\n")
    EOS_list = [t for t in EOS_list if t != ""]
    return EOS_list


def make_morphs(sentence:list()) -> list():
    morphs = []
    for line in sentence:
        morphs = [Morph(i) for i in line.split('\n')\
            if i != "" and i[0] != "*"]
    return morphs

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "ai.ja.txt.parsed")
    with open(filepath, "rt") as f:
        EOS_list = load_file(f)
        morphs = make_morphs(EOS_list)

        for morph in morphs:
            print(morph.make_json())
