import MeCab

def keitaiso():
    filename = '/Users/ohira/100knock2023/souto/chapter04/neko.txt.mecab'
    result = []
    with open(filename, mode='r') as f:
        for line in f:
            if line != 'EOS\n':
                line = line.split('\t')
                if len(line) == 2 and line[0] != '':
                    keitaiso =  line[1].split(',')
                    keitaiso_map = {'surface': line[0], 'base': keitaiso[6], 'pos': keitaiso[0], 'pos1': keitaiso[1]}
                    result.append(keitaiso_map)
            else:
                result.append('EOF')
    return result


if __name__ == '__main__':
    r = keitaiso()
    for i in r:
      print(i)
