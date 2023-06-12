import knock41

s = knock41.sentences
for sentence in s:
    for chunk in sentence.chunks:
        if int(chunk.dst) != -1:
            modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
            modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence.chunks[int(chunk.dst)].morphs])
            print(modifier, modifiee, sep='\t')
    print('\n')