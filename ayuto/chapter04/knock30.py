import io
import sys
import re

with open("neko.txt.mecab", "r") as f:
    _INPUT = f.read()
sys.stdin = io.StringIO(_INPUT)

def knock30():
    ANS=[]
    Dlist=[]
    try:
        while 1:
            S = input()

            #print(S)
            if S == "EOS":
                if Dlist != []:
                    ANS.append(Dlist)
                Dlist=list()
            elif("記号" in S or S == ""): # 空白記号が入った時にバグるので仕方なく記号を除去
                continue
            else:
                word = list(re.split("[\s,]", S))
                D=dict()
                D["surface"] = word[0]
                D["base"] = word[7]
                D["pos"] = word[1]
                D["pos1"] = word[2]
                Dlist.append(D)
    except:
        return ANS

if __name__=="__main__":
    print(knock30())
