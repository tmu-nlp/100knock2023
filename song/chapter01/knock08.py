string = str(input())

split_str = list(string)

encrypt = []
decrypt = []

for i in range(len(split_str)):
    enc = str(split_str[i])
    if enc.islower() == True:
        encrypt.append(chr(219-ord(enc)))
    else:
        encrypt.append(enc)

enc_str = "".join(encrypt)
        
print(enc_str)

for i in range(len(encrypt)):
    dec = str(encrypt[i])
    if dec.islower() == True:
        decrypt.append(chr(219-ord(dec)))
    else:
        decrypt.append(dec)
        
dec_str = "".join(decrypt)
print(dec_str)