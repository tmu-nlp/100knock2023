pat="パトカー"
taxi="タクシー"
marged=""
for i in range(len(pat)): #len(pat)==len(taxi)を仮定
    marged+=pat[i]+taxi[i]
print(marged)
