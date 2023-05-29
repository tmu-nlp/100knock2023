import re
import io
import sys

#入力を標準入力で読む wsl環境じゃないと動かない(なんで?)
with open("ai.ja.txt.parsed", "r") as f:
    _INPUT = f.read()
sys.stdin = io.StringIO(_INPUT)

class Morph:
    """
    1行を読んでobjectを返すクラス
    """
    def __init__(self):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
    def readMorph(self, word) -> object:
        """
        一行の文字列を受け取ってobjectを返す
        """
        splited_word = re.split(r"[\s,]", word)
        #print(splited_word)
        if len(splited_word) == 10:
            self.surface, self.pos, self.pos1, _, _, _ ,_, self.base, _ , _  = splited_word
        else: # AIなどのアルファベット場合
            self.surface, self.pos, self.pos1, _, _, _ ,_, self.base = splited_word
        return self

def read_text_morph() -> list:
    morph_object_list_list = []
    morph_object_list = []
    word = ""
    while True:
        try:
            word = input()
        except:
            break
        if word == "EOS":
            if morph_object_list != []: # EOSが二回続いているときなどに空のリストを入れないように
                morph_object_list_list.append(morph_object_list)
                morph_object_list = []
        # この辺りの処理はreadMorphにさせるべきか否か?
        elif(word[0]==r"*"):
            continue
        else:
            m = Morph() # インスタンス化
            morph_object_list.append(m.readMorph(word))
    return morph_object_list_list

#出力
if __name__ == "__main__":
    print([[o.surface, o.base, o.pos, o.pos1] for o in read_text_morph()[2]])