#輸出結果が間違えた…
import knock41
from knock41 import sentences #句のリスト

with open('knock47.txt','w',encoding='UTF-8') as f:
     for sentence in sentences:
      for chunk in sentence.chunks:
       for morph in chunk.morphs:
        if morph.pos == '動詞': 
          kaku = [] #格
          kou = [] #項
          sa = []
          for src in chunk.srcs:
            if len(sentence.chunks[src].morphs) == 2 and sentence.chunks[src].morphs[0].pos1 == "サ変接続" and sentence.chunks[src].morphs[1].surface == "を":#len2:サ変接続名詞+を
             sa += [''.join([sentence.chunks[src].morphs[0].surface, sentence.chunks[src].morphs[1].surface, morph.base])] #サ変接続名詞＋を＋動詞の基本形
             kaku += [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == '助詞'] #相関する助詞
             kou += [''.join([morph.surface for morph in sentence.chunks[src].morphs if morph.pos != "記号"])] #述語に係っている文節

            if len(kaku) > 1:
             kaku = sorted(kaku) #昇順にソート
             kakus = ' '.join(kaku) #spaceで区切り
             kous =' '.join(kou)
             sas = sorted(sa)
             sas = ' '.join(sas)
             print(f'{sas}\t{kakus}\t{kous}', file = f)