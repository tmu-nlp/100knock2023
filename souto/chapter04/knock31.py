import knock30

def ext_verb():
    r=knock30.keitaiso()
    verb=set()
    for i in r:
        
        if i!='EOF' and i['pos'] == '動詞':
            verb.add(i['surface'])
    return verb

if __name__ == '__main__':
    print(ext_verb())