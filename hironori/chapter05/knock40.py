class Morph():
    def __init__(self, a, b, c, d):
        self.surface = a
        self.base = b
        self.pos = c
        self.pos1 = d
    def prt(self):
        print('[' + self.surface, self.base, self.pos, self.pos1 + ']')

def k40(fi='ai.ja.txt.parsed'):
    with open (fi, encoding='utf-8') as f:
        ans = []
        a = []
        for l in f:
            if l.split()[0] == '*':
                continue
            if l == 'EOS' or l == 'EOS\n':
                if a == []:
                    continue
                ans.append(a)
                a = []
                continue
            d = Morph(l.split('\t')[0], l.split('\t')[1].split(',')[6], l.split('\t')[1].split(',')[0], l.split('\t')[1].split(',')[1])
            a.append(d)
        return ans
            
if __name__=="__main__":
    for i in k40():
        for j in i:
            j.prt()
    