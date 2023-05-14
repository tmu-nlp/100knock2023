import re


def get_mecabed_list(mecabed_text_path: str) -> list:

    with open(mecabed_text_path, 'r', encoding="utf-8") as mecabed_file:
        # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音\n
        pick_pattern = re.compile(
            r"(.*?\t.*?)\n")
        txt = mecabed_file.read()
        lines = re.findall(pick_pattern, txt)
        lines = [re.split(r"[\t,]", line) for line in lines]

        mecabed = []  # 文書全体
        tmplist = []  # 文相当

        for line in lines:  # 形態素辞書構築
            tmpdict = {"surface": "", "base": "", "pos": "", "pos1": ""}  # 形態素
            tmpdict["surface"] = line[0]
            tmpdict["base"] = line[5]
            tmpdict["pos"] = line[1]
            tmpdict["pos1"] = line[2]

            if (tmpdict["surface"] != ''):  # 空文字(neko.txt上では'\n')を除去
                tmplist.append(tmpdict)  # 文に形態素追加

            if (tmpdict["surface"] == '。'):
                mecabed.append(tmplist)
                tmplist = []
    return mecabed


if __name__ == "__main__":
    get_mecabed_list("chapter04/neko.txt.mecab")
