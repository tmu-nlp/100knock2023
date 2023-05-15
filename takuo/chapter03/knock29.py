import requests
import re


def getBaseInfo(fileobj):
    lines = uktxt.readlines()
    # {{基本情報 国 <-flag立てる
    # info <-読む
    # }} <-flag下す

    on_tar = False
    info_dict = {}  # |key = value @uktxt
    for line in lines:
        if (re.match(r'.*基礎情報.*', line)):
            on_tar = True
        if (re.match(r'}}', line)):
            on_tar = False
        if (on_tar and line[0] == '|'):
            # |A = B, |A  =B, |a a = B
            # toupleが1つ返ってくるので，それをkeyvalに渡す．
            keyval = re.findall(r'\|([^=]*) += *(.*)', line)[0]
            info_dict.setdefault(keyval[0], "")
            info_dict[keyval[0]] = keyval[1]
    return info_dict


def getEssence(str):
    rmed_str = re.sub(r"''+", '', str)  # 強調除去

    rmed_str = re.sub(r"\[\[|\]\]|\|.*?\]\]", '', rmed_str)  # 内部リンク除去
    # [[hoge]], [[hoge|piyo]], [[hoge#fuga|piyo]] ->hoge,hoge,hoge#fuga
    rmed_str = re.sub(r"[({{)(}})]", '', rmed_str)  # {{と}}除去
    rmed_str = re.sub(r"<.*?/>", '', rmed_str)  # htmlタグに囲まれた部分除去
    rmed_str = re.sub(r"<ref.*</ref>", '', rmed_str)  # 外部リンク削除
    rmed_str = re.sub(r"ファイル:", '', rmed_str)
    return rmed_str


with open("chapter03/uk_text.txt", 'r') as uktxt:
    baseinfo = getBaseInfo(uktxt)
    for key in baseinfo.keys():
        baseinfo[key] = getEssence(baseinfo[key])
    flag_file = baseinfo["国旗画像"]
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + \
        flag_file + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    flag_url = re.search(r'"url":"(.+?)"', data.text).group(1)
    print(flag_url)
