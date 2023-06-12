import knock41

filename = 'knock43.txt'
with open(filename, mode='w') as f:
    sentences = knock41.sentences
    for sentence in sentences:
        for chunk in sentence.chunks:
            if int(chunk.dst) != -1:
                modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
                modifier_pos = [morph.pos for morph in chunk.morphs]
                modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence.chunks[int(chunk.dst)].morphs])
                modifiee_pos = [morph.pos for morph in sentence.chunks[int(chunk.dst)].morphs]
                if '名詞' in modifier_pos and '動詞' in modifiee_pos:
                    f.write(modifier)
                    f.write('\t')
                    f.write(modifiee)
                    f.write('\n')
        f.write('\n')