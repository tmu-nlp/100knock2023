#31 動詞の表層形の抽出
verbs_surface = []

for lis in neko_list:
  if lis['pos'] =='動詞':
      verbs_surface.append(lis['surface'])

print(len(verbs_surface))
print(verbs_surface[0:5])
