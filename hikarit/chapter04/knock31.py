import knock30


ans = set()
for sentence in knock30.analysis_results:
  for word in sentence:
    if word['pos'] == '動詞':
      ans.add(word['surface'])

for i in list(ans)[0:10]:
  print(i,end="\n")