import re
import json


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


with open("chapter03/uk_text.txt", 'r') as uktxt:
    baseinfo = getBaseInfo(uktxt)
    print(baseinfo)
