import knock30
#import matplotlib

ans = {}

for sentence in knock30.analysis_results:
  for i in sentence:
    if i["pos"] == "記号":
      pass
    elif i["base"] in ans:
      ans[i["base"]]+= 1
    else:
      ans[i["base"]] = 0
ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)

for w in ans[:10]:
  print(w)

