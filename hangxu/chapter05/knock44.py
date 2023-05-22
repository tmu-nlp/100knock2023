import knock41
from knock41 import sentences #句のリスト

import graphviz
from graphviz import Digraph

def plot1(sentence):
 g = Digraph(format='png', filename='knock44')
 g.attr('node', fontname="MS Gothic")
 for chunk in sentence:
  a = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']) #係り元の文節
  b = ''.join([morph.surface for morph in sentence[int(chunk.dst)].morphs if morph.pos != '記号'])  #係り先の文節
  g.edge(a,b)
 g.view()

plot1(sentences[2].chunks)

