import knock30
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"
font_prop = fm.FontProperties(fname=font_path)

ans = {}
Exclusion = ['記号', 'その他', '接頭詞', '助詞', '助動詞', '連体詞']

for sentence in knock30.analysis_results:
  if '猫' in [word['surface'] for word in sentence]:
    for i in sentence:
      if i["pos"] in Exclusion:
        pass
      elif i["base"] == "*\n":
        pass
      elif i["base"] in ans:
        ans[i["base"]]+= 1

      else:
        ans[i["base"]] = 1
ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)

keys = [a[0] for a in ans[0:11]]
values = [a[1] for a in ans[0:11]]

plt.bar(keys, values,  tick_label=keys)
plt.xticks(fontname= font_prop.get_name())

plt.savefig("kncok37.png")

#{'記号', '副詞', '接続詞', '名詞', '動詞', '感動詞', 'フィラー', 'その他', '接頭詞', '助詞', '助動詞', '形容詞', '連体詞'}