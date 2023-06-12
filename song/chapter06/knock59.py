import itertools
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from knock50 import train_df, valid_df, test_df
from knock51 import X_train, X_valid, X_test

def calc_scores(C,solver,class_weight):
    y_train = train_df['CATEGORY']
    y_valid = valid_df['CATEGORY']
    y_test = test_df['CATEGORY']
    
    clf = LogisticRegression(C=C, solver=solver, class_weight=class_weight,  max_iter=10000)
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
solver = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
class_weight = [None, 'balanced']
best_parameter = None
best_scores = None
max_valid_score = 0
for c, s, w in itertools.product(C, solver, class_weight):
    print(c, s, w)
    scores = calc_scores(c, s, w)
    #print (scores)
    if scores[1] > max_valid_score:
        max_valid_score = scores[1]
        best_parameter = [c, s, w]
        best_scores = scores
print ('best patameter: ', best_parameter)
print ('best scores: ', best_scores)
print ('test accuracy: ', best_scores[2])