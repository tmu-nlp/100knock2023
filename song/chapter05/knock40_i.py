import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def read_cabocha_file(file_path):
    sentences = []
    sentence = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('EOS'):
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            elif not line.startswith('*'):
                elements = re.split('[\t,]', line)
                if len(elements) == 10:
                    morph = Morph(elements[0], elements[7], elements[1], elements[2])
                    sentence.append(morph)

    return sentences

file_path = './song/chapter05/ai.ja.txt.parsed'  # Replace with the path to your CaboCha file

output_file = './song/chapter05/knock40.txt'

sentences = read_cabocha_file(file_path)

'''
for morph in sentences[0]:
    print(f'Surface: {morph.surface}\tBase: {morph.base}\tPOS: {morph.pos}\tPOS1: {morph.pos1}')
'''
with open(output_file, "w", encoding="utf-8") as file:
    for morph in sentences[0]:
        file.write(str(f'Surface: {morph.surface}\tBase: {morph.base}\tPOS: {morph.pos}\tPOS1: {morph.pos1}')+'\n')