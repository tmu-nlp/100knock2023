from knock40 import Morph, morph
from itertools import combinations
import re

class Chunk():
  def __init__(self, morphs, dst):
    self.morphs = morphs
    self.dst = dst
    self.srcs = []


class Sentence():
  def __init__(self, chunks):
    self.chunks = chunks
    for i, chunk in enumerate(self.chunks):
      if chunk.dst != -1:
        self.chunks[chunk.dst].srcs.append(i)
        
file_name = './song/chapter05/ai.ja.txt.parsed'

def app_sentence_k49(filename):
  sentences = []
  chunks = []
  morphs = []
  with open(filename, mode='r') as f:
    for line in f:
      if line.startswith('*'):  # 係り受け関係を表す行：直前の文節の情報にChunkを適用し文節リストに追加 + 直後の文節の係り先を取得
        if len(morphs) > 0:
          chunks.append(Chunk(morphs, dst))
          morphs = []
        dst = int(line.split(' ')[2][:-1])
      elif line != 'EOS\n':  # 文末以外：Morphを適用し形態素リストに追加
        morphs.append(Morph(line))
      else:  # 文末：直前の文節の情報にChunkを適用し文節リストに追加 + 文節リストにSentenceを適用し文リストに追加
        chunks.append(Chunk(morphs, dst))
        sentences.append(Sentence(chunks))
        morphs = []
        chunks = []
        dst = None       
  
  sentence = sentences[0]
  nouns = []
  for i, chunk in enumerate(sentence.chunks):
    if '名詞' in [morph.pos for morph in chunk.morphs]:  # 名詞を含む文節を抽出
      nouns.append(i)
  for i, j in combinations(nouns, 2):  # 名詞を含む文節のペアごとにパスを作成
    path_i = []
    path_j = []
    while i != j:
      if i < j:
        path_i.append(i)
        i = sentence.chunks[i].dst
      else:
        path_j.append(j)
        j = sentence.chunks[j].dst
    if len(path_j) == 0:  # 1つ目のケース
      chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence.chunks[path_i[0]].morphs])
      chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence.chunks[i].morphs])
      chunk_X = re.sub('X+', 'X', chunk_X)
      chunk_Y = re.sub('Y+', 'Y', chunk_Y)
      path_XtoY = [chunk_X] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_i[1:]] + [chunk_Y]
      print(' -> '.join(path_XtoY))
    else:  # 2つ目のケース
      chunk_X = ''.join([morph.surface if morph.pos != '名詞' else 'X' for morph in sentence.chunks[path_i[0]].morphs])
      chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence.chunks[path_j[0]].morphs])
      chunk_k = ''.join([morph.surface for morph in sentence.chunks[i].morphs])
      chunk_X = re.sub('X+', 'X', chunk_X)
      chunk_Y = re.sub('Y+', 'Y', chunk_Y)
      path_X = [chunk_X] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_i[1:]]
      path_Y = [chunk_Y] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_j[1:]]
      print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k]))
  return

app_sentence_k49(file_name)

