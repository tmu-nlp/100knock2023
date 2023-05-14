import re

with open("chapter04/neko.txt.mecab", 'r', encoding="utf-8") as mecabed_file:
    # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音\n
    pick_pattern = re.compile(
        r"(.*?\t.*?)\n")
    txt = mecabed_file.read()
    lines = re.findall(pick_pattern, txt)
    lines_spl = [re.split(r"[\t,]", line) for line in lines]

    neko_mecabed = []  # 文書全体
    tmplist = []  # 文相当
    tmpdict = {"surface": "", "base": "", "pos": "", "pos1": ""}  # 形態素
    for line in lines_spl:  # 形態素辞書構築
        tmpdict["surface"] = line[0]
        tmpdict["base"] = line[5]
        tmpdict["pos"] = line[1]
        tmpdict["pos1"] = line[2]

        tmplist.append(tmplist)  # 文に形態素追加
        if (tmpdict["base"] == '。'):
            neko_mecabed.append(tmplist)
            tmplist = []
    print(neko_mecabed)
