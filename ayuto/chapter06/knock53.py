import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression


X_test = pd.read_table("test.feature.txt", header=None)
Y_test = pd.read_table("test.txt", header=None)[1]
lr = pickle.load(open("model.pkl", "rb"))
Y_pred = lr.predict(X_test) 
Y_proba = lr.predict_proba(X_test)
accuracy = 0
for i, pred in enumerate(Y_pred):
    if Y_pred[i] == Y_test[i]:
        accuracy += 1
    y_proba = "{:.3f}".format(max(Y_proba[i]))
    print(f"{i}\t{Y_pred[i]}\t{Y_test[i]}\t{y_proba}")