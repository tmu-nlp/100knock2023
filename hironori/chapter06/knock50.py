import random

class Nad():
    def __init__(self, l):
        dt = l.split('\t')
        self.id = int(dt[0])
        self.title = dt[1]
        self.url = dt[2]
        self.publisher = dt[3]
        self.category = dt[4]
        self.story = dt[5]
        self.hostname = dt[6]
        self.timestamp = dt[7]
    def st(self):
        return "\t".join([str(self.id), self.title, self.url, self.publisher, self.category, self.story, self.hostname, self.timestamp])

def k50(fi='newsCorpora.csv'):
    with open (fi, encoding='utf-8') as f:
        nads = []
        train = []
        valid = []
        test = []
        for l in f:
            if len(l.split('\t')) != 8:
                continue
            a = Nad(l)
            if a.publisher == "Reuters" or a.publisher == "Huffington Post" or a.publisher == "Businessweek" or a.publisher == "Contactmusic.com" or a.publisher == "Daily Mail":
                nads.append(a)
        random.shuffle(nads)
        for i in range(len(nads)):
            if i < len(nads) * 0.8:
                train.append(nads[i])
            elif i < len(nads) * 0.9:
                valid.append(nads[i])
            else:
                test.append(nads[i])
        with open('train.txt', 'w', encoding='utf-8') as fo:
            for i in train:
                print(i.category + "\t" + i.title, file=fo)
        with open('valid.txt', 'w', encoding='utf-8') as fo:
            for i in valid:
                print(i.category + "\t" + i.title, file=fo)
        with open('test.txt', 'w', encoding='utf-8') as fo:
            for i in test:
                print(i.category + "\t" + i.title, file=fo)
        print("全体: " + str(len(nads)))
        print("学習データ: " + str(len(train)))
        print("検証データ: " + str(len(valid)))
        print("評価データ: " + str(len(test)))
                
            
if __name__=="__main__":
    k50()
    