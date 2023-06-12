#これは自分で書くではないから、後でもう一度考える
import knock41
from knock41 import sentences #句のリスト

import re
from itertools import combinations
 
sentence = sentences[2]
nouns = []
for i, chunk in enumerate(sentence.chunks):
  if [morph for morph in chunk.morphs if morph.pos == '名詞']:
    nouns.append(i) #名詞を含む文節のインデックス番号
for i, j in combinations(nouns, 2): #組み合わせ
  path_I = []
  path_J = []
  while i != j:
    if i < j: #文節iの構文木経路上に文節jが存在する
      path_I.append(i)
      i = sentence.chunks[i].dst
    else: #文節iの構文木経路上に文節jがない, i>j,
      path_J.append(j)
      j = sentence.chunks[j].dst
  
  if len(path_J) == 0: # 文節Iの構文木上に文節Jが存在する,i<j
    ##文節iとjに含まれる名詞句をXとYに置換する
    X = "X" + "".join([morph.surface for morph in sentence.chunks[path_I[0]].morphs if morph.pos != "名詞" and morph.pos != "記号"]) 
    Y = "Y" +  "".join([morph.surface for morph in sentence.chunks[i].morphs if morph.pos != "名詞" and morph.pos != "記号"])
    chunk_X = re.sub("X+", "X", X) #置換 
    chunk_Y = re.sub("Y+", "Y", Y)
    path_ItoJ = [chunk_X] + ["".join(morph.surface for n in path_I[1:] for morph in sentence.chunks[n].morphs)] + [chunk_Y]
    print(" -> ".join(path_ItoJ))
  else: # 文節Iの構文木上に文節Jが存在しない
    X = "X" + "".join([morph.surface for morph in sentence.chunks[path_I[0]].morphs if morph.pos != "名詞" and morph.pos != "記号"]) 
    Y = "Y" + "".join([morph.surface for morph in sentence.chunks[path_J[0]].morphs if morph.pos != "名詞" and morph.pos != "記号"]) 
    chunk_X = re.sub("X+", "X", X)
    chunk_Y = re.sub("Y+", "Y", Y)
    chunk_k = "".join([morph.surface for morph in sentence.chunks[i].morphs if morph.pos != "記号"]) #文節iと文節jの構文木の根に至る経路上で交わる文節k
    path_X = [chunk_X] + ["".join(morph.surface for n in path_I[1:] for morph in sentence.chunks[n].morphs if morph.pos != "記号")] #文節iと文節jで、文節kに至るまでのパス
    path_Y = [chunk_Y] + ["".join(morph.surface for n in path_J[1: ]for morph in sentence.chunks[n].morphs if morph.pos != "記号")]
    print(" | ".join(["->".join(path_X), "->".join(path_Y), chunk_k]))