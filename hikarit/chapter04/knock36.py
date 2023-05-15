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
ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)

keys = [a[0] for a in ans[0:10]]
values = [a[1] for a in ans[0:10]]

plt.bar(keys, values,  tick_label=keys)
plt.xticks(fontname= font_prop.get_name())

plt.savefig("kncok36.png")