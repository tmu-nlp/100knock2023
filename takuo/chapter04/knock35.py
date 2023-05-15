from knock30 import get_mecabed_list
from operator import itemgetter

mecabed = get_mecabed_list("chapter04/neko.txt.mecab")

union_dict = {}
for line in mecabed:
    for dic in line:
        union_dict.setdefault(dic["base"], 0)
        union_dict[dic["base"]] += 1
word_freq = sorted(union_dict.items(), key=itemgetter(1), reverse=True)

if __name__=="__main__":
    print(word_freq)
# ('の', 7683), ('。', 7486), ('、', 6772), ('は', 6428), ('を', 6119), ('と', 5974),...