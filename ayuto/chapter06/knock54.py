import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


X_train = pd.read_table("train.feature.txt", header=None)
Y_train = pd.read_table("train.txt", header=None)[1]
X_test = pd.read_table("test.feature.txt", header=None)
Y_test = pd.read_table("test.txt", header=None)[1]
lr = pickle.load(open("model.pkl", "rb"))
train_ac = accuracy_score(Y_train, lr.predict(X_train))
test_ac = accuracy_score(Y_test, lr.predict(X_test))
