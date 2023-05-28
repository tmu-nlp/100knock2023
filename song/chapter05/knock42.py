from knock40 import Morph
from knock41 import read_cabocha_file, listing_src 
import re

file_path = './song/chapter05/ai.ja.txt.parsed'

output_file = './song/chapter05/knock42.py'

sentences = read_cabocha_file(file_path)

sentence = sentences[0]
for chunk in sentence.chunks:
  if int(chunk.dst) != -1:
    modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
    modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence.chunks[int(chunk.dst)].morphs])
    print(modifier, modifiee, sep='\t')