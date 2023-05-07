'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ
'''

src1 = "パトカー"
src2 = "タクシー"

dst = ""
for i in range(len(src1)):
    dst = dst + src1[i]
    dst = dst + src2[i]

print(dst)

# パタトクカシーー
