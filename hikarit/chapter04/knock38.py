import knock30
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
font_prop = fm.FontProperties(fname=font_path)

ans = {}

for sentence in knock30.analysis_results:
  for i in sentence:
    if i["pos"] == "記号":
      pass
    elif i["base"] in ans:
      ans[i["base"]]+= 1
    else:
      ans[i["base"]] = 0
ans = ans.values()
ans = sorted(ans, key=lambda x: x, reverse=True)

plt.hist(ans, bins=50)

plt.savefig("kncok38.png")
