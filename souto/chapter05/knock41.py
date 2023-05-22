class Morph:
  def __init__(self, morph):#一行ずつ読み込んで形態素解析
    surface, attr = morph.split('\t')
    attr = attr.split(',')
    self.surface = surface
    self.base = attr[6]
    self.pos = attr[0]
    self.pos1 = attr[1]

  def print_morph(self):#表示する関数
    print(self.surface + " " + self.base + " " + self.pos + " " + self.pos1)


class Chunk:
  def __init__(self, morphs, line):#一行ずつ読み込んで形態素解析
    self.morphs = morphs
    index=line[2].rstrip('D')
    self.dst = int(index)
    self.srcs = []

  def add_srcs(self, list_srcs):#srcsを追加する関数
    for i in list_srcs:#int型で格納
      self.srcs.append(int(i))

  def print_chunk(self):#表示する関数
    print(str(self.morphs) + " " + str(self.dst) + " " + str(self.srcs))



def keitaiso_and_kakariuke():
  #実際に形態素解析と係り受け解析
  filename = './ai.ja.txt.parsed'
  sentences_morphs = []
  morphs = []
  sentences_chunks=[]#1文ごとのchunkのリストのリスト
  chunks=[]#1文節ごとのchunkのリスト
  morph_bunsetsu=[]#1文節分のmorph

  with open(filename, mode='r') as f:
    kakariukeline=[]
    src=dict()
    for line in f:
      if line[0] == '*':  
        if(kakariukeline!=[]):
          chunks.append(Chunk(morph_bunsetsu,kakariukeline))
          morph_bunsetsu=[]
        kakariukeline = line.split(' ')
        uke=kakariukeline[2].rstrip('D')
        if(uke!='-1'):
          if(uke in src):
            src[uke].append(kakariukeline[1])
          else:
            src[uke]=[kakariukeline[1]]
        
    
      elif line != 'EOS\n':
        morphs.append(Morph(line))
        morph_bunsetsu.append(Morph(line))


      else:
        if(kakariukeline==[]):
          continue

        chunks.append(Chunk(morph_bunsetsu,kakariukeline))
        
        sentences_morphs.append(morphs)

        #ここから係り元文節インデックス番号のリスト（srcs）を決定する
        for key, value in src.items():
          key=int(key)
          chunks[key].add_srcs(value)

        sentences_chunks.append(chunks)
        morphs = []
        chunks=[]
        kakariukeline=[]
        morph_bunsetsu=[]
        src.clear()
  return sentences_morphs, sentences_chunks



if __name__ == '__main__':
  a, b = keitaiso_and_kakariuke()

  for i in b:
    for j in i:#jが１つのchunk
      chunkk="["
      for d in j.morphs:
        chunkk+=d.surface
        chunkk+=", "
      chunkk+="] "
      chunkk+=str(j.dst)+" "
      chunkk+=str(j.srcs)
      print(chunkk)