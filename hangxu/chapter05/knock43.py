import knock41
from knock41 import sentences

for chunk in sentences[2].chunks:
    n = [morph.surface for morph in chunk.morphs if morph.pos == '名詞'] #係り元=名詞
    v = [morph.surface for morph in sentences[2].chunks[int(chunk.dst)].morphs if morph.pos == '動詞'] #係り先=動詞
    a = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']) #係り元の文節
    b = ''.join([morph.surface for morph in sentences[2].chunks[int(chunk.dst)].morphs if morph.pos != '記号'])  #係り先の文節
    
    if n and v: #空ではない
      print(a, b, sep='\t')