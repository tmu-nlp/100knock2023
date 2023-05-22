import knock41
from knock41 import sentences #句のリスト

with open('knock45.txt','w',encoding='UTF-8') as f:
    for i in range(len(sentences)): #各句
     for chunk in sentences[i].chunks:
      for morph in chunk.morphs:
        if morph.pos == '動詞': 
          kaku = []
          for src in chunk.srcs:
            kaku += [morph.surface for morph in sentences[i].chunks[src].morphs if morph.pos == '助詞'] #相関する助詞
          if len(kaku) > 1:
            kaku = sorted(kaku) #昇順にソート
            kakus = ' '.join(kaku) #spaceで区切り
            print(morph.base, kakus, sep='\t', file = f)

## コーパス中で頻出する述語と格パターンの組み合わせ
# cat knock45.txt | sort | uniq -c | sort -nr | head -n 10

##「行う」「なる」「与える」という動詞の格パターン
# cat knock45.txt |grep "行う" | sort |uniq -c | sort -nr |head -n 10
# cat knock45.txt |grep "なる" | sort |uniq -c | sort -nr |head -n 10
# cat knock45.txt |grep "与える" | sort |uniq -c | sort -nr |head -n 10
