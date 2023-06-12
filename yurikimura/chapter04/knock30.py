'''
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）を
MeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

import os

def token_mapping(source):
    dst = []
    with open(source, "rt") as text:
        for line in text:
            dic = {}
            if line != 'EOS\n':
                line = line.replace('\t', ',').split(',')
                if line[0] != '\n':
                    dic["surface"] = line[0]
                    dic["base"] = line[7]
                    dic["pos"] = line[1]
                    dic["pos1"] = line[2]
                    if line[0] != '':
                        dst.append(dic)
    return dst

if __name__ == "__main__":
    neko_mecab = os.path.join(os.path.dirname(__file__), "neko.txt.mecab")
    dst = token_mapping(neko_mecab)
    for data in dst:
        print(data)
