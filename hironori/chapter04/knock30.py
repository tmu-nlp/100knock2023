def k30(fi='neko.txt.mecab'):
    with open (fi, encoding='utf-8') as f:
        ans = []
        a = []
        for l in f:
            if l == '\n' or l.split('\t')[0] == '' or l.split('\t')[0] == '\u3000':
                continue
            if l == 'EOS' or l == 'EOS\n':
                if a == []:
                    continue
                ans.append(a)
                a = []
                continue
            d = {}
            d["surface"] = l.split('\t')[0]
            d["base"] = l.split('\t')[1].split(',')[4]
            d["pos"] = l.split('\t')[1].split(',')[0]
            d["pos1"] = l.split('\t')[1].split(',')[1]
            a.append(d)
        return ans
            
if __name__=="__main__":
    print(k30())
    