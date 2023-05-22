from knock40 import Morph

import re

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

def read_cabocha_file(file_path):
    sentences = []
    sentence = []
    chunks = []
    chunk = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('EOS'):
                if chunk:
                    sentence.append(chunk)
                    chunk = None
                if sentence:
                    sentences.append(sentence)
                    sentence = []
                    chunks = []
            elif line.startswith('*'):
                if chunk:
                    sentence.append(chunk)
                elements = line.split(' ')

                chunk = Chunk([], int(elements[2][:-1]), [])
                chunks.append(int(elements[1]))
            else:
                elements = re.split('[\t,]', line)
                if len(elements) == 10:
                    morph = Morph(elements[0], elements[7], elements[1], elements[2])
                    chunk.morphs.append(morph)
        if sentence:
            for i, chunk in enumerate(chunks):
                if chunk != -1:
                    sentences[-1][chunk].srcs.append(i)

    return sentences

file_path = './song/chapter05/ai.ja.txt.parsed'  # Replace with the path to your CaboCha file

output_file = './song/chapter05/knock41.txt'

sentences = read_cabocha_file(file_path)

'''
for chunk in sentences[2]:
    print(f'Chunk: {"".join([morph.surface for morph in chunk.morphs])}\tDst: {chunk.dst}\tSrcs: {chunk.srcs}')
'''

with open(output_file, "w", encoding="utf-8") as file:
    for chunk in sentences[0]:
        file.write(str(f'Morphs: {" + ".join([morph.surface for morph in chunk.morphs])}\tDst: {chunk.dst}\tSrcs: {chunk.srcs}')+'\n')