# 08. 暗号文Permalink
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(src: str):
    dst = ''
    for c in src:
        if c.islower():
            dst += chr(219-ord(c))
        else:
            dst += c
    return dst

src = input("put any text : ")
print(cipher(src))

# put any text : hogehoge
# sltvsltv
