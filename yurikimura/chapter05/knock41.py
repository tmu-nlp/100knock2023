'''
41. 係り受け解析結果の読み込み（文節・係り受け）Permalink
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を
メンバ変数に持つこととする．さらに，入力テキストの係り受け解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，冒頭の説明文の文節の文字列と係り先を表示せよ．
本章の残りの問題では，ここで作ったプログラムを活用せよ．
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

    def __str__(self):
        return f"表層形:{self.surface}\t基本形:{self.base}\t品詞:{self.pos}\t品詞細分類1:{self.pos1}"

    def make_json(self):
        return {"surface":self.surface, "base":self.base, "pos":self.pos, "pos1":self.pos1}

class Chunk():
    '''
    １文節を形態素のリストとして表現する(morphs)
    係り先のindexをdst、係り元のindexの集まりをsrcsで表現する
    '''
    def __init__(self, morphs:list(), dst:int):
        self.morphs = morphs
        self.dst = dst # 係り先
        self.srcs = [] # 係り元

    def __str__(self):
        surface = ""
        for morph in self.morphs:
            surface += morph.surface
        return f"tsurface:{surface}\tdst:{self.dst}\tsrcs{self.srcs}"

class Sentence():
    '''
    Chunkオブジェクトのsrcs入力のために使用
    指定の文節がどの文節のdst先になっているかをリストで示す
    入力はChunkオブジェクトのリスト
    '''
    def __init__(self, chunks:list()):
        self.chunks = chunks
        for i, chunk in enumerate(chunks):
            if chunk.dst not in [None, -1]:
                self.chunks[chunk.dst].srcs.append(i)


def k41(fname:TextIOWrapper):
    sentences = []  # 文書全体のリスト
    chunks = []  # 一文の文節まとめるリスト
    morphs = []

    with open(fname, "rt") as f:

        for line in f:
            if line[0] == "*":  # morphの情報はなく、dstなどの情報が入っているline
                if len(morphs) > 0: # len(morphs) > 0 であるので、一番始めはない
                    chunks.append(Chunk(morphs, dst))
                    morphs = [] # 初期化
                dst = int(line.split()[2].rstrip('D'))

            elif line != "EOS\n":  # *でもEOSでない時：morphの情報が入っているline
                morphs.append(Morph(line))

            else: # 文末：直前の文節の情報にChunkを適用し文節をSentenceオブジェクトによってsrcsに追加
                chunks.append(Chunk(morphs,dst))
                sentences.append(Sentence(chunks))
                morphs = []
                chunks = []
                dst = None

    return sentences # Sentenceオブジェクト


if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "ai.ja.txt.parsed")
    sentences = k41(filepath)

    for c in sentences[2].chunks:
        print(c)
