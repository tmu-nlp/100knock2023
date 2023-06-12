class Morph:
  def __init__(self, morph):
    surface, attr = morph.split('\t')
    attr = attr.split(',')
    self.surface = surface
    self.base = attr[6]
    self.pos = attr[0]
    self.pos1 = attr[1]


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


# for m in sentences[2]:
#   print(vars(m))