import knock41

a, chunks=knock41.keitaiso_and_kakariuke()#bがchunk

for sentence in chunks:
    for chunk in sentence:
        index=chunk.dst
        if(index==-1):
            continue
        text=""
        for i in chunk.morphs:
            text+=i.surface
        text+="    "
        
        c=sentence[index]
        for i in c.morphs:
            text+=i.surface
        text=text.replace('、', '')
        text=text.replace('。', '')
        text=text.replace('「', '')
        text=text.replace('」', '')
        print(text)

