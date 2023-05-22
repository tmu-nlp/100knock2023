#34 最長一致
#import itertools

noun = []
long_noun = str()
for i in range(len(neko_list)):
    if neko_list[i]['pos'] == '名詞' and neko_list[i+1]['pos'] == '名詞':
      if neko_list[i]['pos'] == '名詞' and neko_list[i-1]['pos'] != '名詞':
        num = 0
        while neko_list[i+num]['pos'] == '名詞':
          long_noun += neko_list[i+num]['surface']
          num += 1
    
    elif neko_list[i]['pos'] == '名詞' and neko_list[i+1]['pos'] != '名詞':
      noun.append(long_noun)
      
    
    else:
      long_noun = str()

noun = list(filter(None, noun))
#確認
print(len(noun))
print(noun[0:100])