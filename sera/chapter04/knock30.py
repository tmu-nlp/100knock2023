def read_mecab(file):
    results = []
    sentence_list = []

    with open(file) as f:
        for line in f:
            if line == "EOS\n":
                if len(sentence_list):
                    results.append(sentence_list)
                    sentence_list = []
            else:
                line1 = line.split('\t')
                line2 = line1[1].split(',')
                sentence = {'surface': line1[0],
                         'base': line2[6],
                         'pos': line2[0],
                         'pos1': line2[1],
                        }
                sentence_list.append(sentence)
    if len(sentence_list):
        results.append(sentence_list)
        sentence_list = []

    return results

if __name__ == "__main__":
    results = read_mecab("neko.txt.mecab")
    print(results[:2])
