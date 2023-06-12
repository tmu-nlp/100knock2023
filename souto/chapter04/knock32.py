import knock30

def ext_verb1():
    r=knock30.keitaiso()
    verb=set()
    for i in range(1, len(r)-1):
        
        if r[i]!='EOF' and r[i]['pos'] == '動詞':
            verb.add(r[i]['base'])
    return verb

if __name__ == '__main__':
    print(ext_verb1())