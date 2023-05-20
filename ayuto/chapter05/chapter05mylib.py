import re
class Morph:
    def __init__(self):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
    def readMorph(self, word):
        self.surface, self.pos, self.pos1,   = re.split(word, r"[\s,]")[:2]
        self.base = re.split(word, r"[\s,]")[7]
    def get(self):
        return((self.surface, self.base, self.pos, self.pos1))