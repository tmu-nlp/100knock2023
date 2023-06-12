#33 AのB
#抽出
noun = []
for i in range(len(neko_list)):
  if neko_list[i]['pos'] == '名詞' and neko_list[i+1]['surface'] == 'の' and neko_list[i+2]['pos'] == '名詞':
      noun.append(neko_list[i]['surface']+neko_list[i+1]['surface']+neko_list[i+2]['surface'])

#確認
print(len(noun))
print(noun[0:5])