from knock40_i import Morph

import re

file_path = './song/chapter05/ai.ja.txt.parsed'  # Replace with the path to your CaboCha file

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

def listing_src(file_path):
    list_of_src = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            
            if line.startswith('*'):
                columns = line.split()
                list_of_src.append(columns[2][:-1])     
        return list_of_src


def read_cabocha_file(file_path):
    
    sentences = []
    sentence = []
    chunks = []
    chunk = None
    list_srcs = listing_src(file_path)
    
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
                
                rest_list = list(filter(lambda x: list_srcs[x] == elements[1], range(len(list_srcs))))
                
                chunk.srcs.extend(rest_list)
                
                
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


output_file = './song/chapter05/knock41.txt'

sentences = read_cabocha_file(file_path)


with open(output_file, "w", encoding="utf-8") as file:
    for chunk in sentences[0]:
        file.write(f'Morphs: {"".join([morph.surface for morph in chunk.morphs])}\t Dst: {chunk.dst}\t Srcs: {chunk.srcs}'+'\n')
        
