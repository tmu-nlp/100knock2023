import knock51
from knock51 import x_train
from knock51 import x_valid
from knock51 import x_test
from knock51 import train
from knock51 import valid
from knock51 import test

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import numpy as np

c = {'C': [0.01, 0.05, 0.1]}

gs_model = GridSearchCV(LogisticRegression(max_iter=1500), c, cv=5, verbose=1)
gs_model.fit(x_train,train['CATEGORY'])

#best parameter
gs_model1 = gs_model.best_estimator_
print(format(gs_model1.score(x_train, train['CATEGORY'])))
print(format(gs_model1.score(x_valid, valid['CATEGORY'])))
print(format(gs_model1.score(x_test, test['CATEGORY'])))
