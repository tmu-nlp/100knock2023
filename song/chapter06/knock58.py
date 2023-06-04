#LogisticRegressionは正則化パラメータCを指定することができます。この値が小さいほど、強い正則化がかかります。

from knock50 import train_df, valid_df, test_df
from knock51 import X_train, X_valid, X_test
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

def calc_scores(c):
    y_train = train_df['CATEGORY']
    y_valid = valid_df['CATEGORY']
    y_test = test_df['CATEGORY']
    
    clf = LogisticRegression(C=c, max_iter=10000)
    clf.fit(X_train, y_train)

    y_train_pred = clf.predict(X_train)
    y_valid_pred = clf.predict(X_valid)
    y_test_pred = clf.predict(X_test)
    
    scores = []
    scores.append(accuracy_score(y_train, y_train_pred))
    scores.append(accuracy_score(y_valid, y_valid_pred))
    scores.append(accuracy_score(y_test, y_test_pred))
    return scores

C = np.logspace(-5, 4, 10, base=10)
scores = []
for c in C:
    scores.append(calc_scores(c))
scores = np.array(scores).T
labels = ['train', 'valid', 'test']

for score, label in zip(scores,labels):
    plt.plot(C, score, label=label)
plt.ylim(0, 1.1)
plt.xscale('log')
plt.xlabel('C', fontsize = 14)
plt.ylabel('Accuracy', fontsize = 14)
plt.tick_params(labelsize=14)
plt.grid(True)
plt.legend()
plt.savefig("./song/chapter06/knock58.png", format="png", dpi=300)