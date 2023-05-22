import knock41
from knock41 import sentences #句のリスト

with open('knock46.txt','w',encoding='UTF-8') as f:
    for i in range(len(sentences)): #各句
     for chunk in sentences[i].chunks:
      for morph in chunk.morphs:
        if morph.pos == '動詞': 
          kaku = []
          kou = []
          for src in chunk.srcs:
            kaku += [morph.surface for morph in sentences[i].chunks[src].morphs if morph.pos == '助詞'] #相関する助詞
            kou += ["".join([morph.surface for morph in sentences[i].chunks[src].morphs if morph.pos != "記号"])] #述語に係っている文節
          if len(kaku) > 1:
            kaku = sorted(kaku) #昇順にソート
            kakus = ' '.join(kaku) #spaceで区切り
            kous =' '.join(kou)
            print(f'{morph.base}\t{kakus}\t{kous}', file = f)