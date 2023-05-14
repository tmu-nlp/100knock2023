import sys
import json

#jsonファイルを引数にとる
args = sys.argv

#辞書型の変数を宣言
country_wiki ={}

#対象のjsonファイルは行ごとのデータ構造（josnl)
#json.loads(l)で各行を辞書として読み込み、
#そのkeyとvalueを新たに宣言した辞書であるcountry_wikiに追加

with open(args[1]) as f:
    for l in f.readlines():
        country_wiki[json.loads(l)["title"]] = json.loads(l)["text"]


print(country_wiki["イギリス"])



#json.loads()　変数に保存されたJSON文字列を読み込む
#json.load()　ディスク上に保存されたJSONファイルを読み込む