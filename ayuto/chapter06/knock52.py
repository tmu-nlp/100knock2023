import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

X_train = pd.read_table("train.feature.txt")
Y_train = pd.read_table("train.txt")["CATEGORY"]

lr = LogisticRegression(random_state=0, max_iter=1000)
lr.fit(X_train, Y_train)
with open("model.pkl", "wb") as f:
        pickle.dump(lr, f)