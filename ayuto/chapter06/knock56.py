import pickle
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score


X_test = pd.read_table("test.feature.txt", header=None)
Y_test = pd.read_table("test.txt", header=None)[1]
lr = pickle.load(open("model.pkl", "rb"))
Y_pred = lr.predict(X_test)
labels = ["b","t","e","m"]
precision = precision_score(Y_test, Y_pred, average=None, labels=labels)
recall = recall_score(Y_test, Y_pred, average=None, labels=labels)
f1 = f1_score(Y_test, Y_pred, average=None, labels=labels)
precision_macro = precision_score(Y_test, Y_pred, average="macro")
recall_macro = recall_score(Y_test, Y_pred, average="macro")
f1_macro = f1_score(Y_test, Y_pred, average="macro")
precision_micro = precision_score(Y_test, Y_pred, average="micro")
recall_micro = recall_score(Y_test, Y_pred, average="micro")
f1_micro = f1_score(Y_test, Y_pred, average="micro")
