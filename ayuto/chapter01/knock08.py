def cipher(x):
    L=list(x)
    for i in range(len(L)):
        if  ord("a") <= ord(L[i]) <=  ord("z"):
            L[i] = chr(219 - ord(L[i]))
    return("".join(L))
# 暗号化
print(cipher("くぁwせdrftgyふじこlp;＠：「」"))
# 復号化 cipher を用いて復号する方法
"""
文字コード表を眺めていると ord(a) + ord(z) = 219 であることに気が付く。
a~zの文字コードが連続していることを考えると、
すなわち219 - 文字コードの処理はすなわちアルファベットの逆順に参照することと対応している
したがってcipherを2回用いたときに文字列は変化しないためcipher()を再度用いることで復号可能
"""
print(cipher("くぁdせwiugtbふじこok;＠：「」"))