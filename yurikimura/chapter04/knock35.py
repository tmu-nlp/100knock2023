'''
35. 単語の出現頻度Permalink
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''

import os
from knock30 import token_mapping

def word_count(dst):
    counts = {}

    for data in dst:
        if data["surface"] in counts.keys():
            counts[data["surface"]] += 1
        else:
            counts[data["surface"]] = 1

    return counts

def pick_value(x):
    return x[1]

neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
dst = token_mapping(neko_mecab)
ans = word_count(dst)
ans = sorted(ans.items(), key=pick_value, reverse=True)
print(ans)

# [('の', 9194), ('て', 6868), ('は', 6420), ('に', 6243),
# ('を', 6071), ('と', 5508), ('が', 5337), ('た', 3988), ...
