import knock41
from knock41 import sentences


for chunk in sentences[2].chunks:
    a = "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"]) #係り元の文節  記号を除く
    b = "".join([morph.surface for morph in sentences[2].chunks[int(chunk.dst)].morphs if morph.pos != "記号"])  #係り先の文節
    print(a, b, sep='\t')
