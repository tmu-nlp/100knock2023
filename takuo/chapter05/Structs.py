import re


class Morph():
    def __init__(self):
        self.surface = None
        self.base = None
        self.pos = None
        self.pos1 = None

    def build(self, mecab_type_string: str):
        morph_items = re.split(r"[\t,]", mecab_type_string)
        # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
        self.surface = morph_items[0]
        self.base = morph_items[7]
        self.pos = morph_items[1]
        self.pos1 = morph_items[2]

    def __str__(self):
        retstr = f"\"surface:{self.surface}, base:{self.base}, pos:{self.pos}, pos1:{self.pos1}\""
        return retstr

    def __repr__(self):
        return self.__str__()


class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = []

    def build(self, header_str: str):
        headinfo = header_str.split(' ')
        self.dst = int(headinfo[2][:-1])

    def add_src(self, src_chunk_id: int):
        self.srcs.append(src_chunk_id)

    def surface(self):
        surface = ""
        for morph in self.morphs:
            surface += morph.surface
        return surface

    def surface_no_punct(self):
        puncts_pattern = re.compile(r'[。、「」『』（）〈〉]*')
        surface = self.surface()
        return re.sub(puncts_pattern, '', surface)

    def __str__(self):

        retstr = f"\"{self.surface()}\" -> {self.dst}"
        return retstr

    def __repr__(self):
        return self.__str__()
