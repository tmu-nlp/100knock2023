import knock30

def num_norm():
    ans=list()
    now=''
    now_num=0
    r=knock30.keitaiso()

    for i in range(0, len(r)):
        
        if r[i]!='EOF' and r[i]['pos'] == '名詞':
            now=now+r[i]['surface']
            now_num=now_num+1
                
        else:
            if(now_num > 1):
                ans.append(now)
                now_num=0
            now=''
            now_num=0
            

    return ans

if __name__ == '__main__':
  print(num_norm())