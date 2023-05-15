import knock30


ans = set()
noun = ""
counter = 0

for sentence in knock30.analysis_results:
  for i in range(0, len(sentence) ):
    if sentence[i]["pos"] == "名詞":
      noun += sentence[i]["surface"]
      counter += 1
    else:
      if counter > 1 :
        ans.add(noun)
      counter = 0
      noun = ""

for i in list(ans)[0:10]:
  print(i,end="\n")
print(f"合計：{len(ans)}")