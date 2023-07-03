import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
from tqdm import tqdm
tqdm.pandas()

countries_df = pd.read_csv('countries.tsv', sep='\t')

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)


conclusion_model_countries = [country for country in countries_df['Country'].tolist() if country in model]
countries_df = countries_df[countries_df['Country'].isin(conclusion_model_countries)].reset_index(drop=True)


countries_vec = [model[country] for country in countries_df['Country'].tolist()]


n = 5
kmeans = KMeans(n_clusters=n, random_state=42)
kmeans.fit(countries_vec)
for i in range(n):
    cluster = np.where(kmeans.labels_ == i)[0]
    print(f'cluster: {i}')
    print(countries_df.iloc[cluster]["Country"].tolist())