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



if __name__ == '__main__':
  #実際に形態素解析
  filename = './ai.ja.txt.parsed'
  sentences = []
  morphs = []
  with open(filename, mode='r') as f:
    for line in f:
      if line[0] == '*':  # 係り受け関係を表す行：スキップ
        continue
      elif line != 'EOS\n':  # 文末以外：Morphを適用し形態素リストに追加
        morphs.append(Morph(line))
      else:  # 文末：形態素リストを文リストに追加
        sentences.append(morphs)
        morphs = []

  #表示
  for morph in sentences:
    for elsement in morph:
      elsement.print_morph()
