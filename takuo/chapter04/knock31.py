from knock30 import get_mecabed_list
mecabed = get_mecabed_list("chapter04/neko.txt.mecab")
for line in mecabed:
    for dic in line:
        if (dic["pos"] == "動詞"):
            print(dic["surface"])
