import knock41

a, chunks=knock41.keitaiso_and_kakariuke()#bがchunk

for sentence in chunks:
    for chunk in sentence:
        f_verb=False
        f_noum=False
        index=chunk.dst
        if(index==-1):
            continue
        text=""
        for i in chunk.morphs:
            text+=i.surface
            if(i.pos=="名詞"):
                f_noum=True
        text+="    "
        
        c=sentence[index]
        for i in c.morphs:
            text+=i.surface
            if(i.pos=="動詞"):
                f_verb=True
        if(f_verb and f_noum):
          text=text.replace('、', '')
          text=text.replace('。', '')
          text=text.replace('「', '')
          text=text.replace('」', '')
          print(text)

