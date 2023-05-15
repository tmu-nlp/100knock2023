from knock30 import get_mecabed_list
mecabed=get_mecabed_list("chapter04/neko.txt.mecab")

for line_idx in range(len(mecabed)):
    for dict_idx in range(len(mecabed[line_idx])-2):
        dic=mecabed[line_idx][dict_idx]
        dic_n=mecabed[line_idx][dict_idx+1]
        dic_nn=mecabed[line_idx][dict_idx+2]
        A_no_B=(dic["pos"]=="名詞"and dic_nn["pos"]=="名詞") and dic_n["pos1"]=="接続助詞"
        if(A_no_B):
            print(dic["surface"]+dic_n["surface"]+dic_nn["surface"])