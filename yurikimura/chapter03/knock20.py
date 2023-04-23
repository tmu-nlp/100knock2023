# 20. JSONデータの読み込みPermalink
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

import json

with open("jawiki-country.json", "r") as my_file:
    with open("20.txt", "w") as wf:
        for line in my_file:
            my_json = json.loads(line)
            if my_json['title'] in "イギリス":
                wf.write(my_json['text'] + '\n')
                print(my_json['text'])
