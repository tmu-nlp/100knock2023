#輸出できない…
import knock41
from knock41 import sentences #句のリスト

def n_path(sentence):
    for chunk in sentence.chunks:
      for morph in chunk.morphs:
        if morph.pos == '名詞':
            path = [''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')] #名詞の文節
            while chunk.dst != -1: #毎句の最後
                path.append(''.join(morph.surface for morph in sentence.chunks[chunk.dst].morphs if morph.pos != '記号')) #パス
            print(' -> '.join(path))

n_path(sentences[2])