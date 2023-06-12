#32 動詞の基本形の抽出
#抽出
verbs_base = []
for lis in neko_list:
  if lis['pos'] =='動詞':
      verbs_base.append(lis['base'])

#確認
print(len(verbs_base))
print(verbs_base[0:5])