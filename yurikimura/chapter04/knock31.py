'''
31. 動詞Permalink
動詞の表層形をすべて抽出せよ．
'''

import os
from knock30 import token_mapping

# def token_mapping(source):
#     dst = []
#     with open(source, "rt") as text:
#         for line in text:
#             dic = {}
#             if line != 'EOS\n':
#                 line = line.replace('\t', ',').split(',')
#                 if line[0] != '\n':
#                     dic["surface"] = line[0]
#                     dic["base"] = line[7]
#                     dic["pos"] = line[1]
#                     dic["pos1"] = line[2]
#                     if line[0] != '':
#                         dst.append(dic)
#     return dst

if __name__ == "__main__":
    # os.path.dirname(__file__) : from/root/to/100knock2023/yurikimura/chapter04
    neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
    dst = token_mapping(neko_mecab)
    for data in dst:
        if data["pos"] == "動詞":
            print(data["surface"])

# 生れ
# つか
# し
# 泣い
# し
# いる
