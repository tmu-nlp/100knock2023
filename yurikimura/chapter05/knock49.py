'''
knock49
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

1. 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を” -> “で連結して表現する
2. 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．

1. 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
2. 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
   文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を” | “で連結して表示
'''
import os
from itertools import combinations
import re
from utils import k41

filepath = os.path.join(os.path.dirname(__file__), "ai.ja.txt.parsed")
sentences = k41(filepath)

sentence = sentences[2] ## Sentenceオブジェクトには1文ごとのChunkオブジェクトが格納されている

nouns = []
for i, chunk in enumerate(sentence.chunks):
  if '名詞' in [morph.pos for morph in chunk.morphs]:
    nouns.append(i) # 名詞を含む文節を抽出

print(combinations(nouns, 2))
for i, j in combinations(nouns, 2):  # 名詞を含む文節のペアごとにpathを作成
  path_i = [] # pathは”index”が格納されている
  path_j = [] # path_jは構造木の根に至るまでに枝分かれしている文節がある場合に格納
  while i != j: # 全てのcombinationが完了してイコールになるまでwhile
    if i < j:
      path_i.append(i)
      i = sentence.chunks[i].dst # chunkが指す次の文節(Chunk)へ更新
    else:
      path_j.append(j)
      j = sentence.chunks[j].dst

  print(f"\npath_i:{path_i}\npath_j{path_j}")

  # 1. 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
  if len(path_j) == 0: # 単方向になるのでpath_jは空のリスト
    print("case1")
    chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' \
        for morph in sentence.chunks[path_i[0]].morphs]) # 名詞ならX, それ以外はsurface
    chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' \
        for morph in sentence.chunks[i].morphs])

    chunk_X = re.sub('X+', 'X', chunk_X) # 同一の文節内に名詞が二つ以上ある場合はXX..となるのでXに置き換え
    chunk_Y = re.sub('Y+', 'Y', chunk_Y)

    path_XtoY = [chunk_X] \
        + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_i[1:]] \
            + [chunk_Y] # path_i[1:]は起点以降の中間のchunks
    print(' -> '.join(path_XtoY)) # listを矢印でjoin

  else:  # 2. 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合
    print("case2")
    chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence.chunks[path_i[0]].morphs])
    chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence.chunks[path_j[0]].morphs])
    chunk_k = ''.join([morph.surface for morph in sentence.chunks[i].morphs])
    chunk_X = re.sub('X+', 'X', chunk_X)
    chunk_Y = re.sub('Y+', 'Y', chunk_Y)
    path_X = [chunk_X] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_i[1:]]
    path_Y = [chunk_Y] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_j[1:]]
    print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k]))
