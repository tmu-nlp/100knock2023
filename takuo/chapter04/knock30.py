import re
neko_mecabed = []
with open("chapter04/neko.txt.mecab", 'r', encoding="utf-8") as mecabed_file:

    # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音\n
    pick_pattern = re.compile(
        r"(.*?\t.*?,.*?,.*?,.*?,.*?,.*?,.*?,.*?,.*?)\n")
    txt = mecabed_file.read()
    lines = re.findall(pick_pattern, txt)
    for l in lines:
        print(l)
