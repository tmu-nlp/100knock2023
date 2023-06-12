'''
32. 動詞の基本形Permalink
動詞の基本形をすべて抽出せよ．
'''

import os
from knock30 import token_mapping

if __name__ == "__main__":
    neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
    dst = token_mapping(neko_mecab)
    for data in dst:
        if data["pos"] == "動詞":
            print(data["base"])
