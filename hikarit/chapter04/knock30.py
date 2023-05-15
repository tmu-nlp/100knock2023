#import MeCab
import re

filename = "neko.txt.mecab"

#空のリストを宣言．analysis_results = 解析結果
analysis_results =[]
sentence = []

with open(filename,"r") as f:
    for l in f.readlines():
        #"neko.txt.mecab"に含まれる、改行やタブなどの不要な要素を排除
        if l == "\n" or l[0] == "\t":
            pass

        #EOSが出た場合，辞書のリストであるsentenceをanalysis_resultsに格納
        elif  l == "EOS\n":
            analysis_results.append(sentence)
            #後の処理に使う変数名なので空の配列にする
            sentence = []

        #re.split()により、複数の文字で行を区切り，sentenceに格納
        else:
            # lの中身：['一', '名詞', '数', '*', '*', '*', '*', '一', 'イチ', 'イチ\n']
            l = re.split("[\t,]",l)
            sentence.append({"surface":l[0],"base":l[7],"pos":l[1],"pos1":l[2]})
            
#確認用
    # for i in analysis_results[0:10]:
    #     for j in i:
    #         print(j,end="\n")
    #     print("\n")
