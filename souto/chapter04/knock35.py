import knock30
import collections

def num_of_tango():
    r=knock30.keitaiso()
    r1=list()
    for i in r:
        if i != 'EOF':
            r1.append(str(i))
    r2 = collections.Counter(r1)
    r2 = sorted(r2.items(), key=lambda x: x[1], reverse=True)
    return r2


if __name__ == '__main__':
    r=num_of_tango()
    for i in range(len(r)):
        print(r[i][0], r[i][1])


