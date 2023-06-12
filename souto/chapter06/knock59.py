import knock41

a, chunks=knock41.keitaiso_and_kakariuke()#bがchunk


with open("./ans49.txt", mode='w') as f:
    for sentence in chunks:
        index_noum_list=[]
        index_noum_list_noum=[]
        for i in range(len(sentence)):

            for j in range(len(sentence[i].morphs)):
                if(sentence[i].morphs[j].pos=="名詞"):
                    if i in index_noum_list:
                        continue
                    index_noum_list.append(i)
                    index_noum_list_noum.append(sentence[i].morphs[j].surface)
                    

        for i in range(len(index_noum_list)):
            for j in range(len(index_noum_list)):
                if(index_noum_list[i]>=index_noum_list[j]):
                    continue
            texti=[]
            textj=[]

            indexi=index_noum_list[i]
            indexj=index_noum_list[j]

            while True:
                if(indexi==-1):
                    break
                textt=""
                for jj in sentence[indexi].morphs:
                    textt+=jj.surface
                texti.append(textt)
                indexi=sentence[indexi].dst

            while True:
                if(indexj==-1):
                    break
                textt=""
                for jj in sentence[indexj].morphs:
                    textt+=jj.surface
                textj.append(textt)
                indexj=sentence[indexj].dst
                


            indexi=index_noum_list[i]
            indexj=index_noum_list[j]

            text_ans=""
            
            if(textj[0] in texti):
                for a in texti:
                    text_ans+=(a+' -> ')
                    if a==textj[0]:
                        text_ans=text_ans.rstrip(' -> ')
                        text_ans=text_ans.split(' -> ')
                        text_ans[0]=text_ans[0].replace(index_noum_list_noum[i], 'X')
                        text_ans[-1]=text_ans[-1].replace(index_noum_list_noum[j], 'Y')
                        text_ans=' -> '.join(text_ans)
                        break
                
            else:
                ff=False
                k=""
                for a in texti:
                    if a in textj:
                        k=a
                        ff=True
                if not(ff):
                    break
                textii=texti[0]+' -> '
                textjj=textj[0]+' -> '
                for a in range(len(texti)):
                    if(texti[a]==k):
                        textii+=texti[a-1]
                for a in range(len(textj)):
                    if(textj[a]==k):
                        textjj+=textj[a-1]
                text_ans=textii + ' | ' + textjj + ' | ' + k
            
                text_ans=text_ans.split('->')
                text_ans[0]=text_ans[0].replace(index_noum_list_noum[i], 'X')
                text_ans[1]=text_ans[1].replace(index_noum_list_noum[j], 'Y')

                text_ans=' -> '.join(text_ans)



            
            text_ans=text_ans.replace('、', '')
            text_ans=text_ans.replace('。', '')
            text_ans=text_ans.replace('「', '')
            text_ans=text_ans.replace('」', '') 
            text_ans=text_ans.replace('（', '')
            text_ans=text_ans.replace('）', '')
            text_ans=text_ans.replace('『', '')
            text_ans=text_ans.replace('』', '')  
            text_ans=text_ans.replace('，', '')    
            f.write(text_ans+'\n')
