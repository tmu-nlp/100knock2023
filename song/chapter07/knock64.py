import gensim
from knock60 import model

with open('/home/nevucide/questions-words.txt') as f:
    questions = f.readlines()
with open('/home/nevucide/knock64.txt','w') as f:
    for i,question in enumerate(questions):
        words = question.split()
        if len(words)==4:
            ans = model.most_similar(positive=[words[1],words[2]], negative=[words[0]],topn=1)[0]
            words += [ans[0], str(ans[1])]
            output = ' '.join(words)+'\n'
        else:
            output = question
        f.write(output)
        if (i%100==0):
            print (i)