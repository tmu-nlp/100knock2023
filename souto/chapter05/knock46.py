import knock41

a, chunks=knock41.keitaiso_and_kakariuke()#bがchunk


with open("./ans46.txt", mode='w') as f:
    for sentence in chunks:
        for chunk in sentence:
            f_josi=False
            f_verb=False
            index=chunk.dst
            if(index==-1):
                continue
            text=[]
            text1=[]
            text_doshi=""
            for i in chunk.morphs:
                if(i.pos=="動詞"):
                    f_verb=True
                    text_doshi=i.base
                    break

            for j in chunk.srcs:
                for k in sentence[j].morphs:
                    if(k.pos=="助詞"):
                        text.append(k.base)
                        f_josi=True
                        text11=""
                        for h in sentence[j].morphs:
                            text11+=h.base
                        text1.append(text11)
                    
            text = sorted(text)
            text1 = sorted(text1)
            

            if(f_verb and f_josi):
                text_ans=text_doshi
                text_ans+='   '
                for i in text:
                    text_ans+=(i+" ")
                for i in text1:
                    text_ans+=(i+" ")
                text_ans=text_ans.rstrip(" ")
                text_ans=text_ans.replace('、', '')
                text_ans=text_ans.replace('。', '')
                text_ans=text_ans.replace('「', '')
                text_ans=text_ans.replace('」', '')
                f.write(text_ans+"\n")
