def cipher(str):
    formatted = ""
    for c in str:
        if (c.islower()):
            code = ord(c)
            formatted += chr(219-code)  # ord(a)+ord(z)==219
        else:
            formatted += c
    return formatted


messages = ["abcdefghijklmnopqrstuvwxyz",
            "Professor (Graduate School of Social Data Science) at Hitotsubashi University."]

for msg in messages:
    print("ciphed:", cipher(msg))  # 暗号化
    print("raw:", cipher(cipher(msg)))  # 復号
