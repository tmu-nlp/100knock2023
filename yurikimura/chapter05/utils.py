from io import TextIOWrapper

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
    def __init__(self, morphs, dst):
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
