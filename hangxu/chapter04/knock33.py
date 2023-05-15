import knock30
from knock30 import result

no = set()

for sentence in result:
    for a in range(len(sentence)):
        if sentence[a]['pos'] == '名詞' and sentence[a+1]['surface'] == 'の' and sentence[a+2]['pos'] == '名詞': 
            no.add(sentence[a]['surface'] + sentence[a+1]['surface'] + sentence[a+2]['surface'])

print(no)