import knock41


filename = 'knock46.txt'
sentences = knock41.sentences
with open(filename, 'w') as f:
  for sentence in sentences:
    for chunk in sentence.chunks:
      for morph in chunk.morphs:
        if morph.pos == '動詞':  # chunkの左から順番に動詞を探す
          cases = []
          modi_chunks = []
          for src in chunk.srcs:  # 見つけた動詞の係り元chunkから助詞を探す
            case = [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == '助詞']
            if len(case) > 0:  # 助詞を含むchunkの場合は助詞と項を取得
              cases = cases + case
              modi_chunks.append(''.join(morph.surface for morph in sentence.chunks[src].morphs if morph.pos != '記号'))
          if len(cases) > 0:  # 助詞が1つ以上見つかった場合は重複除去後辞書順にソートし、項と合わせて出力
            cases = sorted(list(set(cases)))
            line = '{}\t{}\t{}'.format(morph.base, ' '.join(cases), ' '.join(modi_chunks))
            print(line, file=f)
          break