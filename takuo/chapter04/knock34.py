from knock30 import get_mecabed_list
mecabed = get_mecabed_list("chapter04/neko.txt.mecab")

for line_idx in range(len(mecabed)):
    dict_idx = 0
    tmpstr = ""
    count = 0
    while (dict_idx < len(mecabed[line_idx])):
        dic = mecabed[line_idx][dict_idx]
        if (dic["pos"] == "名詞"):
            tmpstr += dic["surface"]
            count += 1

        elif (tmpstr != ""):
            if (count > 8):
                print(tmpstr, count)
            tmpstr = ""
            count = 0
        else:
            tmpstr = ""
            count = 0

        dict_idx += 1
