import knock30


ans = set()
for sentence in knock30.analysis_results:
  for i in range(1, len(sentence) - 1):
    if sentence[i-1]["pos"] == "名詞" and sentence[i]['base'] == 'の' and sentence[i+1]["pos"] == "名詞":
      ans.add(sentence[i-1]['surface'] + sentence[i]['surface'] + sentence[i+1]['surface'])

for i in list(ans)[0:50]:
  print(i,end="\n")