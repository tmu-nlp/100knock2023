'''
42. 係り元と係り先の文節の表示Permalink
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''
import os
from knock41 import k41

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "ai.ja.txt.parsed")
    sentences = k41(filepath)

    for chunk in sentences[2].chunks:
        if int(chunk.dst) != -1: # かかり先がない場合を除いて

            modifier = ''.join([morph.surface if morph.pos != "記号" else ""\
                for morph in chunk.morphs]) # 係り元の文節のsurface(記号以外)のlistをjoin

            # 係り先の文節
            modifiee = ''.join([morph.surface if morph.pos != "記号" else ""\
                for morph in sentences[2].chunks[int(chunk.dst)].morphs])
            # 自分から見た係り先のindex番号を全体から取ってきている

            print(modifier, modifiee, sep='\t')
