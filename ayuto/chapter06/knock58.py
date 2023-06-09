import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#学習データ
X_train = pd.read_table("train.feature.txt", header=None)
Y_train = pd.read_table("train.txt", header=None)[1]
#検証データ
X_valid = pd.read_table("valid.feature.txt", header=None)
Y_valid = pd.read_table("valid.txt", header=None)[1]
#評価データ
X_test = pd.read_table("test.feature.txt", header=None)
Y_test = pd.read_table("test.txt", header=None)[1]
C_list = [1e-2, 1e-1, 1.0, 1e+1, 1e+2]

train_ac = []
valid_ac = []
test_ac = []
for C in C_list:
    lr = LogisticRegression(random_state=0, max_iter=1000, C=C)
    lr.fit(X_train, Y_train)
    train_ac.append(accuracy_score(Y_train, lr.predict(X_train)))
    valid_ac.append(accuracy_score(Y_valid, lr.predict(X_valid)))
    test_ac.append(accuracy_score(Y_test, lr.predict(X_test)))
plt.plot(C_list, train_ac, label="train")
plt.plot(C_list, valid_ac, label="valid")
plt.plot(C_list, test_ac, label="test")
plt.legend()
plt.xscale("log")
plt.savefig("output58.png", format="png")