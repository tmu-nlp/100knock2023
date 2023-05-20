import re
import io
import sys
import re

#入力を標準入力で読む
with open("ai.ja.txt.parsed", "r") as f:
    _INPUT = f.read()
sys.stdin = io.StringIO(_INPUT)

class Morph:
    """
    readMorph(word)でwordをMorphオブジェクトに変換
    readMorph(word).surface でsurfaceを取得できる
    """
    def __init__(self): # メンバ変数を定義(いらないかも)
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
    def readMorph(self, word) -> object:
        self.surface, self.pos, self.pos1,   = re.split(r"[\s,]", word)[:3]
        self.base = re.split(r"[\s,]", word)[7]
        return(self)

def readText():
    morph_object_list_list = []
    morph_object_list = []
    while True:
        try:
            word = input()
        except:
            
            break
        if word == "EOS":
            morph_object_list_list.append(morph_object_list)
            morph_object_list = []
        elif(word[0]==r"*"):
            continue
        else:
            a = Morph() # インスタンス化 毎回インスタンス化しないとバグる
            morph_object_list.append(a.readMorph(word))
    return morph_object_list_list

#出力
if __name__ == "__main__":
    print([[o.surface, o.base, o.pos, o.pos1] for o in readText()[2]])