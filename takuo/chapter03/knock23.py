import re

with open("chapter03/uk_text.txt", 'r') as uktxt:
    txt = uktxt.read()
    # 続く=の数と，=に挟まれた文字列が欲しい
    # =は2以上
    # char+でcahrが一文字以上続く場合にマッチする

    # カーリング，自転車競技の頭尻に' 'が含まれているので，対処
    # 本質的にはr'(==+)([^=]*)==+'
    matched = re.findall(r'(==+) *([^=]*) *==+', txt)

    # クラス名:クラスレベル の辞書に変換
    classes = {}
    for item in matched:
        classes.setdefault(item[1], len(item[0])-1)  # =の数-1がクラスレベル

    for item in classes.items():
        for i in range(item[1]-1):
            print('|', end='')
        print(item[0])
