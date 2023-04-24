p = "パトカー"
t = "タクシー"
pt = ""

for i in range(0,4):
  ptt = (p+t)[i::4] #i=0のときパタ、=1のときトク…となる
  pt += ptt

print(pt)