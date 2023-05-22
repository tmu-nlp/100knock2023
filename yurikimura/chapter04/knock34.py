'''
34. 名詞の連接Permalink
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

import os
from knock30 import token_mapping

if __name__ == "__main__":
    dst = token_mapping("neko.txt.mecab")
    noun_process = []
    noun_ans = []
    for i in range(len(dst)):
        if dst[i]["pos"] == "名詞":
            noun_process.append(dst[i]["surface"])
        elif len(noun_process) >= 2:
            noun_process = "".join(noun_process)
            noun_ans.append(noun_process)
            noun_process = []
        else:
            noun_process = []

    for i in range(len(noun_ans)):
        print(noun_ans[i])
