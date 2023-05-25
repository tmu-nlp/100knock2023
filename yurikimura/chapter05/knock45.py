'''
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「行う」「なる」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''
import os
from utils import k41

filepath = os.path.join(os.path.dirname(__file__), "ai.ja.txt.parsed")
sentences = k41(filepath)

with open('./ans45_py.txt', 'w') as f:
    for sentence in sentences:
        for chunk in sentence.chunks:
            for morph in chunk.morphs:
                if morph.pos == "動詞": # chunkの左から順番に動詞を探す
                    cases = []
                    for src in chunk.srcs: # 見つけた動詞の係り元から助詞を探す
                        cases = cases + \
                            [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == "助詞"]
                    if len(cases) > 0: # 助詞が見つかった場合は重複除去後にソート
                        cases = sorted(list(set(cases)))
                        line = f"{morph.base}\t{' '.join(cases)}"
                        print(line, file=f)
                    break
