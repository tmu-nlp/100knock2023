import knock41

a, chunks=knock41.keitaiso_and_kakariuke()#bがchunk


with open("./ans48.txt", mode='w') as f:
    for sentence in chunks:
        for i in range(len(sentence)):
            f_noum=False
            
            text=[]
            for j in sentence[i].morphs:
                if(j.pos=="名詞"):
                    f_noum=True
                    textt=""
                    for k in sentence[i].morphs:
                        textt+=k.surface
                    text.append(textt)
                    break

            if not(f_noum):
                continue

            index=sentence[i].dst

            while True:
                if(index==-1):
                    break
                textt=""
                for j in sentence[index].morphs:
                    textt+=j.surface
                text.append(textt)
                index=sentence[index].dst
            
                

            text_ans=' -> '.join(text)
            text_ans=text_ans.replace('、', '')
            text_ans=text_ans.replace('。', '')
            text_ans=text_ans.replace('「', '')
            text_ans=text_ans.replace('」', '') 
            text_ans=text_ans.replace('（', '')
            text_ans=text_ans.replace('）', '')
            text_ans=text_ans.replace('『', '')
            text_ans=text_ans.replace('』', '')  
            text_ans=text_ans.replace('，', '')           
            f.write(text_ans+"\n")