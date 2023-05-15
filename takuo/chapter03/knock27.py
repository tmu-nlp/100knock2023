
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

# def remove_markup(text):
#     pattern = r'\'{2,5}'
#     text = re.sub(pattern, '', text)

#     pattern = r'\[\[(?:[^|]*?\|)*?([^|]*?)*?\]\]' # <-ここすげえ，(|以外の文字+|)が最小個 + (|以外の文字)でグループ作って，\1で1番目のグループを参照している，スゲー！！！
#     text = re.sub(pattern, r'\1', text)

#     return text


with open("chapter03/uk_text.txt", 'r') as uktxt:
    baseinfo = getBaseInfo(uktxt)
    for key in baseinfo.keys():
        rmed_str = re.sub(r"''+", '', baseinfo[key])  # 'が二個以上続いたら置換
        # [[hoge]], [[hoge|piyo]], [[hoge#fuga|piyo]] ->hoge,hoge,hoge#fuga
        rmed_str = re.sub(r"\[\[|\]\]|\|.*\]\]", '', rmed_str)
        baseinfo[key] = rmed_str

    print(baseinfo)  # 確立形態3とか
