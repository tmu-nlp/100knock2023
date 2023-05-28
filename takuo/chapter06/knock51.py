import re
import os


def rm_punct(text: str) -> str:
    '''remove ,.[]{}"'`!?():;'''
    puncts = re.compile(r"[,.\[\]{}\"'`!?\(\):;]")
    return re.sub(puncts,  '', text)


def get_words_list(sentence: str) -> list:
    worded = re.split(r"[\t \n]", sentence)
    lowered = []
    for w in worded:
        tmpstr = rm_punct(w)
        tmpstr = tmpstr.lower()
        lowered.append(tmpstr)
    return lowered[1:-1]


def gen_features_txt(input_filepath: str, output_filepath: str):
    worded = []
    with open(f"{input_filepath}", 'r') as rawfile:
        for l in rawfile.readlines():
            worded.append(get_words_list(l))

    with open(f"{output_filepath}", 'w') as out:
        for data in worded:
            stred = ' '.join(data)
            out.write(stred+'\n')


trainfile = os.path.dirname(__file__)+"/train.txt"
train_feat = os.path.dirname(__file__)+"/train.feature.txt"
validfile = os.path.dirname(__file__)+"/valid.txt"
valid_feat = os.path.dirname(__file__)+"/valid.feature.txt"
testfile = os.path.dirname(__file__)+"/test.txt"
test_feat = os.path.dirname(__file__)+"/test.feature.txt"
gen_features_txt(trainfile, train_feat)
gen_features_txt(validfile, valid_feat)
gen_features_txt(testfile, test_feat)
