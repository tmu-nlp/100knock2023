from knock40 import Morph, morph

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

def app_sentence_k48(filename):
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
  for chunk in sentence.chunks:
    if '名詞' in [morph.pos for morph in chunk.morphs]:  # chunkが名詞を含むか確認
      path = [''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')]
      while chunk.dst != -1:  # 名詞を含むchunkを先頭に、dstを根まで順に辿ってリストに追加
        path.append(''.join(morph.surface for morph in sentence.chunks[chunk.dst].morphs if morph.pos != '記号'))
        chunk = sentence.chunks[chunk.dst]
      print(' -> '.join(path))  
  return

app_sentence_k48(file_name)

