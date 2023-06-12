from knock40 import Morph, morph
'''
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

def app_sentence_k46(filename):
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
        '''
  
  with open('./song/chapter05/ans46.txt', 'w') as f:
    for sentence in sentences:
      for chunk in sentence.chunks:
        for morph in chunk.morphs:
          if morph.pos == '動詞':  # chunkの左から順番に動詞を探す
            cases = []
            modi_chunks = []
            for src in chunk.srcs:  # 見つけた動詞の係り元chunkから助詞を探す
              case = [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == '助詞']
              if len(case) > 0:  # 助詞を含むchunkの場合は助詞と項を取得
                cases = cases + case
                modi_chunks.append(''.join(morph.surface for morph in sentence.chunks[src].morphs if morph.pos != '記号'))#記号以外のものall append
            if len(cases) > 0:  # 助詞が1つ以上見つかった場合は重複除去後辞書順にソートし、項と合わせて出力
              cases = sorted(list(set(cases)))
              line = '{}\t{}\t{}'.format(morph.base, ' '.join(cases), ' '.join(modi_chunks))
            print(line, file=f)
          break
  return

app_sentence_k46(file_name)

