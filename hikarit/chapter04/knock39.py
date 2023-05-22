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

ranks = [r + 1 for r in range(len(ans))]
plt.scatter(ranks, ans)
plt.xscale('log')
plt.yscale('log')

plt.savefig("kncok39.png")
