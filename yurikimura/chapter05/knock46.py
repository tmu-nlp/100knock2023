'''
knock46
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

1. 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
2. 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。」という例文を考える．
この文は「作り出す」という１つの動詞を含み，
「作り出す」に係る文節は「ジョン・マッカーシーは」，「会議で」，「用語を」であると解析された場合は，
次のような出力になるはずである．

作り出す	で は を	会議で ジョンマッカーシーは 用語を
'''
import os
from utils import k41

filepath = os.path.join(os.path.dirname(__file__), "ai.ja.txt.parsed")
sentences = k41(filepath)

with open('./ans46_py.txt', 'w') as f:
    for sentence in sentences:
        for chunk in sentence.chunks:
            for morph in chunk.morphs:
                if morph.pos == "動詞": # chunkの左から順番に動詞を探す
                    cases = []
                    modi_chunks = []
                    for src in chunk.srcs: # 見つけた動詞の係り元から助詞を探す
                        a_case = [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == "助詞"]
                        if len(a_case) > 0:
                            cases = cases + a_case
                            modi_chunks.append(''.join([morph.surface for morph in sentence.chunks[src].morphs if morph.pos != "記号"]))

                    if len(cases) > 0: # 助詞が見つかった場合は重複除去後にソート
                        cases = sorted(list(set(cases)))
                        line = f"{morph.base}\t{' '.join(cases)}\t{' '.join(modi_chunks)}"
                        print(line, file=f)
                    break
