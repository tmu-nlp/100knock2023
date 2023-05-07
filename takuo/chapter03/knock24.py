import re

with open("chapter03/uk_text.txt", 'r') as uktxt:
    lines = uktxt.readlines()
    matched = []
    # for line in lines:
    #     # ファイル:filename.hoge|~~~

    matched.append(re.findall(
        'ファイル:(.*.+)[^\|]', "ファイル:Heathrow Terminal 5C Iwelumo-1.jpg|thumb|[[:en:London Heathrow Terminal 5|London Heathrow Terminal 5]]. [[ロンドン・ヒースロー空港]]は[[:en:World's busiest airports by international passenger traffic|国際線利用客数]]では世界随一である。]][[ファイル:Airbus A380-841 G-XLEB British Airways (10424102995).jpg|thumb|ブリティッシュ・エアウェイズ (イギリス最大の航空会社)]]"))
    print(matched)
