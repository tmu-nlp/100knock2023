'''
News Aggregator Data Setをダウンロードし、以下の要領で学習データ（train.txt），検証データ（valid.txt），評価データ（test.txt）を作成せよ．

ダウンロードしたzipファイルを解凍し，readme.txtの説明を読む．
情報源（publisher）が”Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
抽出された事例をランダムに並び替える．
抽出された事例の80%を学習データ，残りの10%ずつを検証データと評価データに分割し，それぞれtrain.txt，valid.txt，test.txtというファイル名で保存する．ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのタブ区切り形式とせよ（このファイルは後に問題70で再利用する）．
学習データと評価データを作成したら，各カテゴリの事例数を確認せよ．
'''
# データの入手・整形
import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    #read_csvでquoting=3を指定するとクオート文字を特別扱いしない
    df = pd.read_csv("newsCorpora.csv", sep="\t", header=None, quoting=3)
    df.columns = ["ID","TITLE","URL","PUBLISHER","CATEGORY","STORY","HOSTNAME","TIMESTAMP"]

    # 情報源（publisher）が”Reuters”, “Huffington Post”,
    # “Businessweek”, “Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
    df = df[df["PUBLISHER"].isin(["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"])]

    # 抽出された事例をランダムに並び替える．
    #frac=1でランダムに，randomstateで乱数シードを固定
    df = df.sample(frac=1, random_state=0)

    # 抽出された事例の80%を学習データ，残りの10%ずつを検証データと評価データに分割
    train, val_test = train_test_split(df, test_size=0.2)
    valid, test = train_test_split(val_test, test_size=0.5)

    # それぞれtrain.txt，valid.txt，test.txtというファイル名で保存する．
    # ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのタブ区切り形式とせよ
    train.to_csv("train.txt", columns=["TITLE","CATEGORY"], sep="\t", header=None, index=False)
    valid.to_csv("valid.txt", columns=["TITLE","CATEGORY"], sep="\t", header=None, index=False)
    test.to_csv("test.txt", columns=["TITLE","CATEGORY"], sep="\t", header=None, index=False)

"""
% wc train.txt
   10682  122335  716434 train.txt
% wc test.txt
    1334   15336   89510 test.txt
% wc valid.txt
    1334   15311   89022 valid.txt
"""
