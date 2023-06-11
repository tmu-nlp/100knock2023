from sklearn.cluster import KMeans
from knock60 import model

with open('/home/nevucide/country.txt','r') as f:
    lines = f.readlines()
countries = []
for line in lines:
    country = line.split('　')[-1].replace('\n','')
    countries.append(country)
dic = {'United States of America':'United_States', 'Russian Federation':'Russia'}
ng = 0
vec = []
target_countries = []
for c in countries:
    for k,v in dic.items():
        c = c.replace(k,v)
    c = c.replace(' ','_').replace('-','_').replace('_and_','_')
    try:
        
        vec.append(model[c])
        target_countries.append(c)
    except:
        ng += 1
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(vec)
for c,l in zip(target_countries, kmeans.labels_):
    print (c,l)