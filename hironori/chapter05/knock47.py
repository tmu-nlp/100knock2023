from knock40 import Morph
from knock41 import Chunk, k41
           
for sc in k41(): # 1文を取り出す
    for c in range(len(sc)): # 1文から1チャンクを取り出す
        txt = ''
        sahenwo = []
        if any(m.pos == '動詞' for m in sc[c].morphs): # 動詞を含む文節なら
            flg = False
            ch = {}
            for m in sc[c].morphs: # 1チャンクから最左の動詞を取り出す
                if m.pos == '動詞':
                    txt = m.base + '\t'
                    break
            for cn in sc[c].srcs: # 述語に係る文節を取り出す
                if any(sc[cn].morphs[mn-1].pos1 == 'サ変接続' and sc[cn].morphs[mn].base == 'を' and sc[cn].morphs[mn].pos == '助詞' for mn in range(1,len(sc[cn].morphs))): # 述語に係る文節が「サ変接続名詞+を（助詞）」なら
                    for md in range(1,len(sc[cn].morphs)):
                        if sc[cn].morphs[md-1].pos1 == 'サ変接続' and sc[cn].morphs[md].base == 'を' and sc[cn].morphs[md].pos == '助詞':
                            if len(sahenwo) == 0:
                                sahenwo = [sc[cn].morphs[md-1].surface, sc[cn].morphs[md].surface]
                                flg = True
                            else:
                                ch[''.join(sahenwo)] = sahenwo[1]
                                sahenwo = [sc[cn].morphs[md-1].surface, sc[cn].morphs[md].surface]
                elif any(m.pos == '助詞' for m in sc[cn].morphs): # 述語に係る文節が助詞を含むなら
                    s = []
                    k = ''
                    for md in sc[cn].morphs: # 記号以外の単語を文節から取り出す
                        if md.pos != '記号':
                            s.append(md.surface)
                        if md.pos == '助詞' and k == '':
                            k = md.base
                            ch[''.join(s)] = k
            srt = sorted(ch.items(), key=lambda x: x[1])
            pars = []
            for cla, par in srt:
                if par not in pars:
                    pars.append(par)
            txt = ''.join(sahenwo) + txt + ' '.join(pars) + '\t' + ' '.join(k[0] for k in srt)
            if flg:
                print(txt)