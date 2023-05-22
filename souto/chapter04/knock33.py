import knock30

def ext_norm_no_norm():
    r=knock30.keitaiso()
    norm_no_norm=set()
    for i in range(1, len(r)-1):
        
        if r[i]!='EOF' and r[i]['surface'] == 'の':
            if(r[i-1]!='EOF' and r[i-1]['pos'] == '名詞' and r[i+1]!='EOF' and r[i+1]['pos'] == '名詞'):
                norm_no_norm.add(r[i-1]['surface']+r[i]['surface']+r[i+1]['surface'])
    return norm_no_norm

if __name__ == '__main__':
    print(ext_norm_no_norm())