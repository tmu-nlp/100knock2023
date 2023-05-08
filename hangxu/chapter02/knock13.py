with open('col1.txt','r') as f1:
    with open('col2.txt','r') as f2:
        with open('col1+2.txt','w') as f3:
          for col1, col2 in zip(f1, f2):
            f3.write('{0}\t{1}\n'.format(col1.strip(), col2.strip()))

#strip():spaceをキャンセルする