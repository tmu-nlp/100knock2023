from knock52 import clf
from knock51 import vectorizer
from knock50 import train_df

dic = {'b':'business', 't':'science and technology', 'e' : 'entertainment', 'm' : 'health'}
def predict(text):
    text = [text]
    X = vectorizer.transform(text)
    ls_proba = clf.predict_proba(X)
    for proba in ls_proba:
        for c, p in zip(clf.classes_, proba):
            print (dic[c]+':',p)
s = train_df.iloc[0]['TITLE']
print(s)
predict(s)